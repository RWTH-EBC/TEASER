"""holds functions to create a report for a TEASER project model"""

import html
import os
import csv
from collections import OrderedDict

import plotly.graph_objects as go


def localize_floats(row):
    return [str(el).replace(".", ",") if isinstance(el, float) else el for el in row]


def create_model_report(prj, path):
    """Creates model report for the project.

    This creates a html and .csv model report for each building of the project
    for easier analysis of the created buildings. Currently only the basic
    values for areas and U-values and an abstracted 3D visualization are part of
    the report. Wall constructions and similar things might come in the future.

    Parameters
    ----------

    prj : Project
        project that the report should be created for
    path : string
        path of the base project export

    """

    prj_data = OrderedDict()
    for bldg in prj.buildings:
        bldg_name = bldg.name
        prj_data[bldg_name] = OrderedDict()
        # create keys
        if bldg.type_of_building:
            prj_data[bldg_name]["Type of Building"] = bldg.type_of_building
        prj_data[bldg_name]["Net Ground Area"] = bldg.net_leased_area
        prj_data[bldg_name]["Ground Floor Area"] = 0
        prj_data[bldg_name]["Roof Area"] = 0
        prj_data[bldg_name]["Floor Height"] = bldg.height_of_floors
        prj_data[bldg_name]["Number of Floors"] = bldg.number_of_floors
        prj_data[bldg_name]["Total Air Volume"] = bldg.volume
        prj_data[bldg_name]["Number of Zones"] = len(bldg.thermal_zones)
        prj_data[bldg_name]["Year of Construction"] = bldg.year_of_construction
        prj_data[bldg_name]["Calculated Heat Load"] = bldg.sum_heat_load
        prj_data[bldg_name]["Calculated Cooling Load"] = bldg.sum_cooling_load

        # todo use bldg.*_names if existing

        prj_data[bldg_name]["Outerwall Area"] = {}
        outer_wall_area_total = 0

        outer_areas = bldg.outer_area
        # make sure that lowest values of orient come first
        sorted_keys = sorted(outer_areas.keys())
        sorted_outer_areas = {key: outer_areas[key] for key in sorted_keys}
        for orient in sorted_outer_areas:
            # some archetypes use floats, some integers for orientation in
            # TEASER
            orient = float(orient)
            if orient == -1:
                prj_data[bldg_name]["Roof Area"] += sorted_outer_areas[orient]
            elif orient == -2:
                prj_data[bldg_name]["Ground Floor Area"] += sorted_outer_areas[orient]
            else:
                if orient not in prj_data[bldg_name]["Outerwall Area"]:
                    prj_data[bldg_name]["Outerwall Area"][orient] = 0
                prj_data[bldg_name]["Outerwall Area"][orient] += sorted_outer_areas[
                    orient
                ]
                outer_wall_area_total += sorted_outer_areas[orient]
        window_area_total = 0
        prj_data[bldg_name]["Outerwall Area Total"] = outer_wall_area_total
        prj_data[bldg_name]["Window Area"] = {}

        window_areas = bldg.window_area
        # make sure that lowest values of orient come first
        sorted_keys = sorted(window_areas.keys())
        sorted_window_areas = {key: window_areas[key] for key in sorted_keys}

        for orient in sorted_window_areas:
            orient = float(orient)
            if orient not in prj_data[bldg_name]["Window Area"]:
                prj_data[bldg_name]["Window Area"][orient] = 0
            prj_data[bldg_name]["Window Area"][orient] += sorted_window_areas[orient]
            window_area_total += sorted_window_areas[orient]

        prj_data[bldg_name]["Window Area Total"] = window_area_total
        prj_data[bldg_name]["Window-Wall-Ratio"] = (
            window_area_total / outer_wall_area_total
        )
        prj_data[bldg_name]["Inner Wall Area"] = bldg.get_inner_wall_area()

        u_values_win = []
        g_values_windows = []
        u_values_ground_floor = []
        u_values_inner_wall = []
        u_values_outer_wall = []
        u_values_door = []
        u_values_roof = []
        u_values_ceiling = []
        for tz in bldg.thermal_zones:
            for window in tz.windows:
                u_values_win.append(1 / (window.r_conduc * window.area))
                g_values_windows.append(window.g_value)
            for inner_wall in tz.inner_walls:
                u_values_inner_wall.append(1 / (inner_wall.r_conduc * inner_wall.area))
            for outer_wall in tz.outer_walls:
                u_values_outer_wall.append(1 / (outer_wall.r_conduc * outer_wall.area))
            for rooftop in tz.rooftops:
                u_values_roof.append(1 / (rooftop.r_conduc * rooftop.area))
            for ground_floor in tz.ground_floors:
                u_values_ground_floor.append(
                    1 / (ground_floor.r_conduc * ground_floor.area)
                )
            for ceiling in tz.ceilings:
                u_values_ceiling.append(1 / (ceiling.r_conduc * ceiling.area))
            for floor in tz.floors:
                u_values_ceiling.append(1 / (floor.r_conduc * floor.area))
            for door in tz.doors:
                u_values_door.append(1 / (door.r_conduc * door.area))
        if len(u_values_outer_wall) > 0:
            prj_data[bldg_name]["UValue Outerwall"] = sum(u_values_outer_wall) / len(
                u_values_outer_wall
            )
        else:
            prj_data[bldg_name]["UValue Outerwall"] = 0
        if len(u_values_inner_wall) > 0:
            prj_data[bldg_name]["UValue Innerwall"] = sum(u_values_inner_wall) / len(
                u_values_inner_wall
            )
        else:
            prj_data[bldg_name]["UValue Innerwall"] = 0

        if len(u_values_win) > 0:
            prj_data[bldg_name]["UValue Window"] = sum(u_values_win) / len(u_values_win)
        else:
            prj_data[bldg_name]["UValue Window"] = 0

        if len(u_values_door) > 0:
            prj_data[bldg_name]["UValue Door"] = sum(u_values_door) / len(u_values_door)
        else:
            prj_data[bldg_name]["UValue Door"] = 0

        if len(u_values_roof) > 0:
            prj_data[bldg_name]["UValue Roof"] = sum(u_values_roof) / len(u_values_roof)
        else:
            prj_data[bldg_name]["UValue Roof"] = 0

        if len(u_values_ceiling) > 0:
            prj_data[bldg_name]["UValue Ceiling"] = sum(u_values_ceiling) / len(
                u_values_ceiling
            )
        else:
            prj_data[bldg_name]["UValue Ceiling"] = 0

        if len(u_values_ground_floor) > 0:
            prj_data[bldg_name]["UValue Groundfloor"] = sum(
                u_values_ground_floor
            ) / len(u_values_ground_floor)
        else:
            prj_data[bldg_name]["UValue Groundfloor"] = 0
        if len(g_values_windows) > 0:
            prj_data[bldg_name]["gValue Window"] = sum(g_values_windows) / len(
                g_values_windows
            )
        else:
            prj_data[bldg_name]["gValue Window"] = 0

        bldg_data = prj_data[bldg_name]

        export_reports(bldg_data, bldg_name, path, prj)


def export_reports(bldg_data, bldg_name, path, prj):
    if not os.path.exists(path):
        os.mkdir(path)
        os.mkdir(os.path.join(path, "plots"))
    base_name = f"{prj.name}_{bldg_name}"
    output_path_base = os.path.join(path, base_name)
    plotly_file_name = os.path.join(path, "plots", base_name + "_plotly.html")
    # Draw an abstract image of the building and save it with plotly to HTML
    interactive_fig, fixed_height =\
        create_simple_3d_visualization(bldg_data, roof_angle=30)
    if interactive_fig:
        interactive_fig.write_html(plotly_file_name)
    else:
        plotly_file_name = None
    html_file_name = os.path.join(output_path_base + ".html")
    create_html_page(
        bldg_data, prj.name, bldg_name, html_file_name, plotly_file_name,
        fixed_height)
    create_csv_report(bldg_data, output_path_base)


def create_csv_report(bldg_data, output_path_base):
    # flat the keys

    prj_data_flat = {}
    for key, val in bldg_data.items():
        if isinstance(bldg_data[key], dict):
            for subkey in bldg_data[key].keys():
                prj_data_flat[str(key) + "_" + f"{subkey:03}"] = bldg_data[key][subkey]
        else:
            prj_data_flat[key] = bldg_data[key]

    bldg_add_list = {"OuterWall": [], "Window": []}
    for key in prj_data_flat.keys():
        if key.startswith("Outerwall Area_"):
            bldg_add_list["OuterWall"].append(key)
        if key.startswith("Window Area_"):
            bldg_add_list["Window"].append(key)
    bldg_add_list["OuterWall"].sort()
    bldg_add_list["Window"].sort()

    bldg_sorted_list = [
        "Net Ground Area",
        "Number of Zones" "Ground Floor Area",
        "Roof Area",
        "Floor Height",
        "Number of Floors",
        "Total Air Volume",
        *bldg_add_list["OuterWall"],
        *bldg_add_list["Window"],
        "Window-Wall-Ratio",
        "Inner Wall Area",
        "UValue Outerwall",
        "UValue Innerwall",
        "UValue Window",
        "UValue Door",
        "UValue Roof",
        "UValue Ceiling",
        "UValue Groundfloor",
        "gValue Window",
    ]
    # round values
    for key, value in prj_data_flat.items():
        if not value:
            value = "-"
        elif not isinstance(value, str):
            prj_data_flat[key] = round(value, 2)
        else:
            prj_data_flat[key] = value
    bldg_data_flat_sorted = [
        (k, prj_data_flat[k]) for k in bldg_sorted_list if k in prj_data_flat.keys()
    ]

    keys = [""]
    keys.extend([x[0] for x in bldg_data_flat_sorted])

    values = ["TEASER"]
    values.extend([x[1] for x in bldg_data_flat_sorted])

    csv_file_name = os.path.join(output_path_base + ".csv")
    with open(csv_file_name, "w", newline="", encoding="utf-8") as f:
        csvwriter = csv.writer(f, delimiter=";")
        csvwriter.writerow(keys)
        csvwriter.writerow(localize_floats(values))


def add_compass_to_3d_plot(fig, x_y_axis_sizing):
    lines = [
        ((0, x_y_axis_sizing - 1, 0), (0, x_y_axis_sizing, 0), "<b>N</b>"),
        ((x_y_axis_sizing - 1, 0, 0), (x_y_axis_sizing, 0, 0), "<b>E</b>"),
        ((0, -x_y_axis_sizing + 1, 0), (0, -x_y_axis_sizing, 0), "<b>S</b>"),
        ((-x_y_axis_sizing + 1, 0, 0), (-x_y_axis_sizing, 0, 0), "<b>W</b>"),
    ]

    for start, end, label in lines:
        fig.add_trace(
            go.Scatter3d(
                x=[start[0], end[0]],
                y=[start[1], end[1]],
                z=[start[2], end[2]],
                mode="lines+text",
                line=dict(color="black"),
                hoverinfo="none",
                showlegend=False,
            )
        )
        fig.add_trace(
            go.Scatter3d(
                x=[end[0]],
                y=[end[1]],
                z=[end[2]],
                mode="text",
                text=[label],
                textposition="top center",
                hoverinfo="none",
                showlegend=False,
            )
        )

        arrow_length = 1
        arrow_color = "black"

        arrow = go.Cone(
            x=[end[0]],
            y=[end[1]],
            z=[end[2]],
            u=[end[0] - start[0]],
            v=[end[1] - start[1]],
            w=[end[2] - start[2]],
            sizemode="absolute",
            sizeref=arrow_length,
            showscale=False,
            colorscale=[[0, arrow_color], [1, arrow_color]],
            hoverinfo="none",
        )
        fig.add_trace(arrow)

    # Set layout
    fig.update_layout(scene=dict(aspectmode="manual", aspectratio=dict(x=1, y=1, z=1)))
    return fig


def create_html_page(bldg_data, prj_name, bldg_name, html_file_name,
                     iframe_src, fixed_height):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{html.escape(prj_name)} - {html.escape(bldg_name)}</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
                padding: 20px;
            }}
            .container {{
                background-color: #ffffff;
                border: 1px solid #e2e2e2;
                border-radius: 5px;
                padding: 20px;
                box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                text-align: center;
                margin-bottom: 20px;
            }}
            table {{
                border-collapse: collapse;
            }}
            th, td {{
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #dee2e6;
            }}
            th {{
                background-color: #f8f9fa;
            }}
            .red-bg {{
                background-color: #f44336;
                color: #ffffff;
            }}
            .iframe-container {{
                border: 1px solid #e2e2e2;
                border-radius: 5px;
                padding: 0px;
            }}
            iframe {{
                width: 100%;
                height: 600px;
                border: none;
            }}
            .legend {{
                margin-top: 10px;
                font-size: 14px;
            }}
        </style>
    </head>
    <body>
        <h1 class="red-bg py-2">{
    html.escape(prj_name)} - {html.escape(bldg_name)}</h1>
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <table class="table table-bordered">
    """

    current_category = None
    for key, value in bldg_data.items():
        unit = "-"
        category = None
        list_item = False
        # Handle category names
        if (
            "window" in key.lower() or "wall" in key.lower()
        ) and "uvalue" not in key.lower():
            category = "Wall and Window Areas"
            unit = "m²"
        elif key.startswith("UValue") or key.startswith("Gvalue"):
            category = "U-Values (mean)"
            unit = ["kW", "kg K"]
        elif key in [
            "Net Ground Area",
            "Roof Area",
            "Floor Height",
            "Number of Floors",
            "Total Air Volume",
            "Number of Zones",
            "Year of Construction",
            "Type of Building",
        ]:
            category = "Base Values"
            unit = "m²"
        elif key.startswith("Calculated"):
            category = "Calculated Values"
            unit = "W"

        if key.lower() in [
            "number of floors",
            "number of zones",
            "year of construction",
            "window-wall-ratio",
            "gvalue window",
            "type of building",
        ]:
            unit = "-"
        if key.lower() == "total air volume":
            unit = "m³"
        if key.lower() == "floor height":
            unit = "m"
        if category and category != current_category:
            html_content += f"""
                    <tr class="table-secondary">
                        <th colspan="3">{html.escape(category)}</th>
                    </tr>
                """
            if category == "Wall and Window Areas":
                html_content += """
                    <tr>
                        <td colspan="2">(0° := North, 90° := East,
                         180° := South, 270° := West)</td>
                    </tr>
                """
            current_category = category

        # handle subdict for outerwall and window area with directions
        if key == "Outerwall Area" or key == "Window Area":
            list_item = True
            for orient, area in bldg_data[key].items():
                value = area
                html_content += f"""
                    <tr>
                    <th scope="row">{html.escape(str(key))}
                        {html.escape(str(orient))}</th>
                 <td>{html.escape(
                    str(round(value, 2)))} </td>
                <td style=
                    "text-align: center; background-color: #D3D3D3;">
                                        {html.escape(unit)}</td>
                </tr>
                    """
        else:
            key_human_readable = " ".join(
                [word.capitalize() for word in key.split("_")]
            )
            html_content += f"""
                    <tr>
                        <th scope="row">{html.escape(key_human_readable)}</th>
                        """
            if not isinstance(value, str):
                if value:
                    value = str(round(value, 2))
                else:
                    value = "-"
        if not list_item:
            html_content += f"""
                <td>{html.escape(value)} </td>
                    <td style=
                        "text-align: center; background-color: #D3D3D3;">
                    """
            if isinstance(unit, list):
                html_content += f"""
                        {html.escape(unit[0])} <frac> {html.escape(unit[1])}</td>
                    </tr>
                """
            else:
                html_content += f"""
                        {html.escape(unit)}</td>
                    </tr>
                """
    if iframe_src:
        html_content += f"""
            </table>
                </div>
                <div class="col-md-6">
                  <div class="iframe-container">
                      <iframe src="{iframe_src}"></iframe>
                          <div class="legend">
                             <span class="badge badge-light"
    style="background-color: gray;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
    Walls
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <span class="badge badge-light"
    style="background-color: blue;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
    Windows <br>"""
    else:
        html_content += f"""
                                </table>
                            </div>
                            <div class="col-md-6">
                                <div class="iframe-container">
                                    <p style="color:Red"><b>Error: No graphic
                                    available.
                                    Error during image creation.</b> <br></p>"""
    html_content += f"""
                    <i>Assumptions</i>: <br>
                    <li><i>All windows of a storey and with the same
                    orientation are put together into one big window
                    which is placed in the middle of the storey</i></li>
                    <li><i>Only works for buildings with 4 directions currently,
                     while the smallest will be interpreted as
                    north, the next bigger one as east and so on.</i></li>
                    <li><i>The roof is not displayed correctly yet</i></li>"""
    if fixed_height:
        html_content += f"""<li><i>The height of all floors is assumed to be 3
        meters.</i></li>"""
    html_content += f"""
                </div>
              </div>
            </div>
        </div>
    </body>
</html>
"""

    with open(html_file_name, "w") as html_file:
        html_file.write(html_content)


def create_simple_3d_visualization(bldg_data, roof_angle=30):
    """Creates a simplified 3d plot of the building.

    This is for a rough first visual analysis of the building and is mostly
    relevant for buildings that are created "manual" and not for archetypes.
    The simplified visualization has multiple assumptions/simplifications:
    * All windows of a storey and with the same orientation are put together
    into one big window which is placed in the middle of the storey
    * Only works for buildings with 4 directions currently, while the smallest
    will be interpreted as north, the next bigger one as east and so on.
    * Orientations are
        Positive y: North
        Positive x: East
        Negative y: South
        Negative x: West
    * The roof is not displayed correctly yet # TODO
    """

    def get_value_with_default(lst, index, default_value):
        try:
            return lst[index]
        except IndexError:
            return default_value

    try:
        area_values = list(bldg_data["Outerwall Area"].values())
        window_values = list(bldg_data["Window Area"].values())
        # TODO: use orientations as well and "turn" the vertices based on this.
        #  Currently the first value (which is the smallest) will be taken as
        #  north, the next one as east and so on. Only the first 4 values are
        #  taken into account.
        area_north = get_value_with_default(area_values, 0, 0)
        area_east = get_value_with_default(area_values, 1, 0)
        area_south = get_value_with_default(area_values, 2, 0)
        area_west = get_value_with_default(area_values, 3, 0)
        window_area_north = get_value_with_default(window_values, 0, 0)
        window_area_east = get_value_with_default(window_values, 1, 0)
        window_area_south = get_value_with_default(window_values, 2, 0)
        window_area_west = get_value_with_default(window_values, 3, 0)
        height = bldg_data["Floor Height"]
        fixed_height = False
        if not height:
            height = 3
            fixed_height = True
        num_floors = bldg_data["Number of Floors"]

        length_north = area_north / (num_floors * height)
        length_east = area_east / (num_floors * height)
        length_south = area_south / (num_floors * height)
        length_west = area_west / (num_floors * height)

        fig = go.Figure()

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=5, r=5, b=5, t=0),
            scene=dict(
                xaxis=dict(
                    gridcolor="white",
                    showbackground=False,
                    zerolinecolor="white",
                ),
                yaxis=dict(
                    gridcolor="white", showbackground=False, zerolinecolor="white"
                ),
                zaxis=dict(
                    gridcolor="white", showbackground=False, zerolinecolor="white"
                ),
                aspectmode="cube",
                xaxis_showgrid=False,
                yaxis_showgrid=False,
                zaxis_showgrid=False,
                xaxis_title="",
                yaxis_title="",
                zaxis_title="",
            ),
        )

        max_length = max(length_north, length_south, length_west, length_east)
        x_y_axis_sizing = (max_length / 2) * 1.1
        fig.update_layout(
            scene=dict(
                xaxis=dict(range=[-x_y_axis_sizing, x_y_axis_sizing]),
                yaxis=dict(range=[-x_y_axis_sizing, x_y_axis_sizing]),
                zaxis=dict(range=[0, max_length]),
            )
        )
        fig = add_compass_to_3d_plot(fig, x_y_axis_sizing)
        for floor in range(num_floors):
            # Ecken des aktuellen Stockwerks
            floor_height = height * floor
            vertices = [
                (-length_south / 2, -length_east / 2, floor_height),
                (-length_south / 2 + length_north, -length_east / 2, floor_height),
                (
                    -length_south / 2 + length_north,
                    -length_east / 2 + length_west,
                    floor_height,
                ),
                (-length_south / 2, -length_east / 2 + length_west, floor_height),
                (-length_south / 2, -length_east / 2, floor_height + height),
                (
                    -length_south / 2 + length_north,
                    -length_east / 2,
                    floor_height + height,
                ),
                (
                    -length_south / 2 + length_north,
                    -length_east / 2 + length_west,
                    floor_height + height,
                ),
                (
                    -length_south / 2,
                    -length_east / 2 + length_west,
                    floor_height + height,
                ),
            ]

            edges = [
                # 0: bottom
                [vertices[0], vertices[1], vertices[2], vertices[3], vertices[0]],
                # 1: top
                [vertices[4], vertices[5], vertices[6], vertices[7], vertices[4]],
                # 2: south
                [vertices[0], vertices[1], vertices[5], vertices[4], vertices[0]],
                # 3: north
                [vertices[2], vertices[3], vertices[7], vertices[6], vertices[2]],
                # 4: east
                [vertices[1], vertices[2], vertices[6], vertices[5], vertices[1]],
                # 5: west
                [vertices[4], vertices[7], vertices[3], vertices[0], vertices[4]],
            ]

            # Add walls as 3D polygons with color fill
            for edge in edges:
                xs, ys, zs = zip(*edge)
                fig.add_trace(
                    go.Mesh3d(
                        x=xs,
                        y=ys,
                        z=zs,
                        i=[0, 0, 1, 0],
                        j=[1, 2, 2, 3],
                        k=[2, 3, 3, 1],
                        opacity=0.25,
                        color="gray",
                        hoverinfo="none",
                    )
                )

            # Fenster hinzufügen
            window_gap_top_bottom = 0.5
            for i, (window_area, wall_vertices) in enumerate(
                zip(
                    [
                        window_area_north,
                        window_area_east,
                        window_area_south,
                        window_area_west,
                    ],
                    [edges[3], edges[4], edges[2], edges[5]],
                )
            ):
                window_height = height - window_gap_top_bottom
                window_width = window_area / (num_floors * window_height)
                window_x_center = (
                    wall_vertices[0][0]
                    + (wall_vertices[1][0] - wall_vertices[0][0]) / 2
                )
                window_y_center = (
                    wall_vertices[0][1]
                    + (wall_vertices[2][1] - wall_vertices[0][1]) / 2
                )
                window_z_center = (
                    floor_height + window_gap_top_bottom / 2 + window_height / 2
                )

                if i == 0 or i == 2:
                    fig.add_trace(
                        go.Mesh3d(
                            x=[
                                window_x_center - window_width / 2,
                                window_x_center + window_width / 2,
                                window_x_center + window_width / 2,
                                window_x_center - window_width / 2,
                            ],
                            y=[
                                window_y_center,
                                window_y_center,
                                window_y_center,
                                window_y_center,
                            ],
                            z=[
                                window_z_center - window_height / 2,
                                window_z_center - window_height / 2,
                                window_z_center + window_height / 2,
                                window_z_center + window_height / 2,
                            ],
                            i=[0, 0, 1, 0],
                            j=[1, 2, 2, 3],
                            k=[2, 3, 3, 1],
                            opacity=0.7,
                            color="blue",
                            hoverinfo="none",
                        )
                    )
                else:
                    fig.add_trace(
                        go.Mesh3d(
                            x=[
                                window_x_center,
                                window_x_center,
                                window_x_center,
                                window_x_center,
                            ],
                            y=[
                                window_y_center - window_width / 2,
                                window_y_center + window_width / 2,
                                window_y_center + window_width / 2,
                                window_y_center - window_width / 2,
                            ],
                            z=[
                                window_z_center - window_height / 2,
                                window_z_center - window_height / 2,
                                window_z_center + window_height / 2,
                                window_z_center + window_height / 2,
                            ],
                            i=[0, 0, 1, 0],
                            j=[1, 2, 2, 3],
                            k=[2, 3, 3, 1],
                            opacity=0.7,
                            color="blue",
                            hoverinfo="none",
                        )
                    )

        return fig, fixed_height
    except Exception as e:
        message = type(e).__name__ + str(e.args)
        print(
            f"An error occured during creating the simplified plot for model "
            f"report. Will continue without plot. Error: {message}: "
        )
        return None
