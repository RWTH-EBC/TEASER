"""holds functions to create a report for a TEASER project model"""

import html
import os
import csv
import plotly.graph_objects as go


def localize_floats(row):
    return [
        str(el).replace('.', ',') if isinstance(el, float) else el
        for el in row
    ]


def calc_report_data(prj, path):
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

    prj_data = {}
    for bldg in prj.buildings:
        bldg_name = bldg.name
        prj_data[bldg_name] = {}
        # create keys
        prj_data[bldg_name]['Roof Area'] = 0
        prj_data[bldg_name]['Ground Floor Area'] = 0
        # prj_data[bldg_name]['CalculatedHeatLoad'] = bldg.sum_heat_load
        # prj_data[bldg_name]['CalculatedCoolingLoad'] = bldg.sum_cooling_load
        prj_data[bldg_name]['Net ground area'] = bldg.net_leased_area
        prj_data[bldg_name]['Total Air Volume'] = bldg.volume
        # prj_data[bldg_name]['YearOfConstruction'] = bldg.year_of_construction
        prj_data[bldg_name]['Inner Wall Area'] = bldg.get_inner_wall_area()
        # if bldg.type_of_building:
        #     prj_data[bldg_name]['TypeOfBuilding'] = bldg.type_of_building
        # todo use bldg.*_names if existing
        prj_data[bldg_name]['Floor Height'] = bldg.height_of_floors
        prj_data[bldg_name]['Number of Floors'] = bldg.number_of_floors

        prj_data[bldg_name]['Outerwall Area'] = {}
        outer_wall_area_total = 0
        for orient in bldg.outer_area:
            # some archetypes use floats, some integers for orientation in
            # TEASER
            orient = float(orient)
            if orient == -1:
                prj_data[bldg_name]['Roof Area'] += bldg.outer_area[orient]
            elif orient == -2:
                prj_data[bldg_name]['Ground Floor Area'] += \
                    bldg.outer_area[orient]
            else:
                if orient not in \
                        prj_data[bldg_name]['Outerwall Area']:
                    prj_data[bldg_name]['Outerwall Area'][orient] = 0
                prj_data[bldg_name]['Outerwall Area'][orient] += \
                    bldg.outer_area[orient]
                outer_wall_area_total += bldg.outer_area[orient]
        window_area_total = 0
        prj_data[bldg_name]['Window Area'] = {}
        for orient in bldg.window_area:
            orient = float(orient)
            if orient not in prj_data[bldg_name]['Window Area']:
                prj_data[bldg_name]['Window Area'][orient] = 0
            prj_data[bldg_name]['Window Area'][orient] += \
                bldg.window_area[orient]
            window_area_total += bldg.window_area[orient]
        prj_data[bldg_name]['Window Area_Total'] = window_area_total
        prj_data[bldg_name]['Outerwall Area_Total'] = outer_wall_area_total
        prj_data[bldg_name][
            'Window-Wall-Ratio'] = window_area_total / outer_wall_area_total
        prj_data[bldg_name]['nZones'] = len(bldg.thermal_zones)
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
                u_values_inner_wall.append(
                    1 / (inner_wall.r_conduc * inner_wall.area))
            for outer_wall in tz.outer_walls:
                u_values_outer_wall.append(
                    1 / (outer_wall.r_conduc * outer_wall.area))
            for rooftop in tz.rooftops:
                u_values_roof.append(
                    1 / (rooftop.r_conduc * rooftop.area))
            for ground_floor in tz.ground_floors:
                u_values_ground_floor.append(
                    1 / (ground_floor.r_conduc * ground_floor.area))
            for ceiling in tz.ceilings:
                u_values_ceiling.append(
                    1 / (ceiling.r_conduc * ceiling.area))
            for floor in tz.floors:
                u_values_ceiling.append(
                    1 / (floor.r_conduc * floor.area))
            for door in tz.doors:
                u_values_door.append(
                    1 / (door.r_conduc * door.area))
        if len(u_values_outer_wall) > 0:
            prj_data[bldg_name]['UValue Outerwall'] = sum(u_values_outer_wall) \
                                                      / len(u_values_outer_wall)
        else:
            prj_data[bldg_name]['UValue Outerwall'] = 0

        if len(u_values_inner_wall) > 0:
            prj_data[bldg_name]['UValue Innerwall'] = sum(u_values_inner_wall) \
                                                      / len(u_values_inner_wall)
        else:
            prj_data[bldg_name]['UValue Innerwall'] = 0

        if len(u_values_win) > 0:
            prj_data[bldg_name]['UValue Window'] = sum(u_values_win) \
                                                   / len(u_values_win)
        else:
            prj_data[bldg_name]['UValue Window'] = 0

        if len(u_values_door) > 0:
            prj_data[bldg_name]['UValue Door'] = sum(u_values_door) \
                                                 / len(u_values_door)
        else:
            prj_data[bldg_name]['UValue Door'] = 0

        if len(u_values_roof) > 0:
            prj_data[bldg_name]['UValue Roof'] = sum(u_values_roof) \
                                                 / len(u_values_roof)
        else:
            prj_data[bldg_name]['UValue Roof'] = 0

        if len(u_values_ceiling) > 0:
            prj_data[bldg_name]['UValue Ceiling'] = sum(u_values_ceiling) \
                                                    / len(u_values_ceiling)
        else:
            prj_data[bldg_name]['UValue Ceiling'] = 0

        if len(u_values_ground_floor) > 0:
            prj_data[bldg_name]['UValue Groundfloor'] = sum(
                u_values_ground_floor) \
                                                        / len(
                u_values_ground_floor)
        else:
            prj_data[bldg_name]['UValue Groundfloor'] = 0

        if len(g_values_windows) > 0:
            prj_data[bldg_name]['gValue Window'] = sum(g_values_windows) \
                                                   / len(g_values_windows)
        else:
            prj_data[bldg_name]['gValue Window'] = 0

        # flat the keys
        bldg_data = prj_data[bldg_name]
        prj_data_flat = {}
        for key, val in bldg_data.items():
            if isinstance(bldg_data[key], dict):
                for subkey in bldg_data[key].keys():
                    prj_data_flat[str(key) + '_' + f"{subkey:03}"] = \
                        bldg_data[key][
                            subkey]
            else:
                prj_data_flat[key] = bldg_data[key]

        bldg_add_list = {'OuterWall': [], 'Window': []}
        for key in prj_data_flat.keys():
            if key.startswith('Outerwall Area_'):
                bldg_add_list['OuterWall'].append(key)
            if key.startswith('Window Area_'):
                bldg_add_list['Window'].append(key)
        bldg_add_list['OuterWall'].sort()
        bldg_add_list['Window'].sort()

        bldg_sorted_list = [
            'Net Ground Area',
            'nZones'
            'Ground Floor Area',
            'Roof Area',
            'Floor Height',
            'Number of Floors',
            'Total Air Volume',
            *bldg_add_list['OuterWall'],
            *bldg_add_list['Window'],
            'Window-Wall-Ratio',
            'Inner Wall Area',
            'UValue Outerwall',
            'UValue Innerwall',
            'UValue Window',
            'UValue Door',
            'UValue Roof',
            'UValue Ceiling',
            'UValue Groundfloor',
            'gValue Window',

        ]
        # round values
        for key, value in prj_data_flat.items():
            prj_data_flat[key] = round(value, 2)

        bldg_data_flat_sorted = [
            (k, prj_data_flat[k]) for k in bldg_sorted_list if
            k in prj_data_flat.keys()]

        # Draw an abstract image of the building and save it with plotly to HTML
        interactive_fig = create_simple_3d_visualization(
            area_north=prj_data_flat["Outerwall Area_0.0"],
            area_east=prj_data_flat["Outerwall Area_90.0"],
            area_south=prj_data_flat["Outerwall Area_180.0"],
            area_west=prj_data_flat["Outerwall Area_270.0"],
            height=prj_data_flat["Floor Height"],
            window_area_north=prj_data_flat["Window Area_0.0"],
            window_area_east=prj_data_flat["Window Area_90.0"],
            window_area_south=prj_data_flat["Window Area_180.0"],
            window_area_west=prj_data_flat["Window Area_270.0"],
            num_floors=prj_data_flat["Number of Floors"],
            roof_angle=30)

        keys = ['']
        keys.extend([x[0] for x in bldg_data_flat_sorted])

        values = ['TEASER']
        values.extend([x[1] for x in bldg_data_flat_sorted])

        export_report(
            bldg_data_flat_sorted,
            bldg_name,
            interactive_fig,
            keys,
            path,
            prj,
            values)


def export_report(bldg_data_flat_sorted, bldg_name, interactive_fig, keys, path,
                  prj, values):
    if not os.path.exists(path):
        os.mkdir(path)
        os.mkdir(os.path.join(path, "plots"))
    base_name = f"{prj.name}_{bldg_name}"
    output_path_base = os.path.join(path, base_name)
    plotly_file_name = os.path.join(path, "plots", base_name + '_plotly.html')
    interactive_fig.write_html(plotly_file_name)
    html_file_name = os.path.join(output_path_base + '.html')
    create_html_page(
        bldg_data_flat_sorted,
        prj.name,
        bldg_name,
        html_file_name,
        plotly_file_name)
    csv_file_name = os.path.join(output_path_base + '.csv')
    with open(csv_file_name, 'w', newline='',
              encoding='utf-8') as f:
        csvwriter = csv.writer(f, delimiter=';')
        csvwriter.writerow(keys)
        csvwriter.writerow(localize_floats(values))


def create_html_page(
        prj_data_tuples,
        prj_name, bldg_name,
        html_file_name,
        iframe_src):
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
                padding: 20px;
            }}
            iframe {{
                width: 100%;
                height: 500px;
                border: none;
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
    for key, value in prj_data_tuples:
        category = None

        # Handle category names
        if key.startswith("Outerwall Area_") or key.startswith("Window Area_"):
            category = "Wall and Window Areas"
        elif key.startswith("UValue"):
            category = "U-Values"
        elif key == "Outerwall Area_Total":
            category = "Total Wall Area"
        elif key == "Window Area_Total":
            category = "Total Window Area"
        elif key in [
            "Net ground area",
            "Roof Area", "Floor Height", "Number of Floors",
            "Total Air Volume"]:
            category = "Base Values"

        if category and category != current_category:
            html_content += f"""
                        <tr class="table-secondary">
                            <th colspan="2">{html.escape(category)}</th>
                        </tr>
                    """
            current_category = category

        key_human_readable = ' '.join(
            [word.capitalize() for word in key.split('_')])

        html_content += f"""
                <tr>
                    <th scope="row">{html.escape(key_human_readable)}</th>
                    <td>{html.escape(str(value))}</td>
                </tr>
            """

    html_content += f"""
                    </table>
                </div>
                <div class="col-md-6">
                    <div class="iframe-container">
                        <iframe src="{iframe_src}"></iframe>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    with open(html_file_name, 'w') as html_file:
        html_file.write(html_content)


def create_simple_3d_visualization(
        area_north, area_east,
        area_south, area_west,
        height, num_floors=1,
        roof_angle=30,
        window_area_north=0,
        window_area_east=0,
        window_area_south=0,
        window_area_west=0):
    """Creates a simplified 3d plot of the building.

    This is for a rough first visual analysis of the building and is mostly
    relevant for buildings that are created "manual" and not for archetypes.
    The simplified visualization has multiple assumptions/simplifications:

    * All windows of a storey and with the same orientation are put together
    into one big window which is placed in the middle of the storey
    * The roof is not displayed correctly # TODO
     """
    length_north = area_north / (num_floors * height)
    length_east = area_east / (num_floors * height)
    length_south = area_south / (num_floors * height)
    length_west = area_west / (num_floors * height)

    fig = go.Figure()

    for floor in range(num_floors):
        # Ecken des aktuellen Stockwerks
        floor_height = height * floor
        vertices = [
            (0, 0, floor_height),
            (length_south, 0, floor_height),
            (length_south, length_east, floor_height),
            (length_south - length_north, length_west, floor_height),
            (0, 0, floor_height + height),
            (length_south, 0, floor_height + height),
            (length_south, length_east, floor_height + height),
            (length_south - length_north, length_west, floor_height + height),
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
            fig.add_trace(go.Mesh3d(x=xs, y=ys, z=zs,
                                    i=[0, 0, 1, 0],
                                    j=[1, 2, 2, 3],
                                    k=[2, 3, 3, 1],
                                    opacity=0.25, color='gray'))

        # Fenster hinzufügen
        window_gap_top_bottom = 0.5
        for i, (window_area, wall_vertices) in enumerate(zip(
                [window_area_north, window_area_east,
                 window_area_south, window_area_west],
                [edges[3], edges[4], edges[2], edges[5]])):
            num_windows_on_side = int(window_area / num_floors)
            window_height = height - window_gap_top_bottom
            window_width = window_area / (num_floors * window_height)
            window_x_center = wall_vertices[0][0] + (
                    wall_vertices[1][0] - wall_vertices[0][0]) / 2
            window_y_center = wall_vertices[0][1] + (
                    wall_vertices[2][1] - wall_vertices[0][1]) / 2
            window_z_center = floor_height + window_gap_top_bottom / \
                              2 + window_height / 2

            if i == 0 or i == 2:
                fig.add_trace(go.Mesh3d(x=[window_x_center - window_width / 2,
                                           window_x_center + window_width / 2,
                                           window_x_center + window_width / 2,
                                           window_x_center - window_width / 2],
                                        y=[window_y_center, window_y_center,
                                           window_y_center, window_y_center],
                                        z=[window_z_center - window_height / 2,
                                           window_z_center - window_height / 2,
                                           window_z_center + window_height / 2,
                                           window_z_center + window_height / 2],
                                        i=[0, 0, 1, 0],
                                        j=[1, 2, 2, 3],
                                        k=[2, 3, 3, 1],
                                        opacity=0.7, color='blue'))
            else:
                fig.add_trace(go.Mesh3d(
                    x=[window_x_center, window_x_center, window_x_center,
                       window_x_center],
                    y=[window_y_center - window_width / 2,
                       window_y_center + window_width / 2,
                       window_y_center + window_width / 2,
                       window_y_center - window_width / 2],
                    z=[window_z_center - window_height / 2,
                       window_z_center - window_height / 2,
                       window_z_center + window_height / 2,
                       window_z_center + window_height / 2],
                    i=[0, 0, 1, 0],
                    j=[1, 2, 2, 3],
                    k=[2, 3, 3, 1],
                    opacity=0.7, color='blue'))

    return fig
