import html
import os
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import plotly.graph_objects as go


"""holds functions to create a report for a TEASER project model"""


# orient_mapper = {
#     0: 'North',
#     90: 'East',
#     180: 'South',
#     270: 'West'
# }
# todo orientations not work yet correctly
def orient_mapper(angle):
    orient = None
    if angle <= 45 or 315 < angle <= 360:
        orient = 'North'
    elif 45 < angle <= 135:
        orient = 'East'
    elif 135 < angle <= 225:
        orient = 'South'
    elif 225 < angle <= 315:
        orient = 'West'
    return orient


def localize_floats(row):
    return [
        str(el).replace('.', ',') if isinstance(el, float) else el
        for el in row
    ]


def calc_report_data(prj, path, name=None):
    prj_data = {}
    for bldg in prj.buildings:
        bldg_name = bldg.name
        prj_data[bldg_name] = {}
        # create keys
        prj_data[bldg_name]['RoofArea'] = 0
        prj_data[bldg_name]['GroundFloorArea'] = 0
        # prj_data[bldg_name]['CalculatedHeatLoad'] = bldg.sum_heat_load
        # prj_data[bldg_name]['CalculatedCoolingLoad'] = bldg.sum_cooling_load
        prj_data[bldg_name]['NetGroundArea'] = bldg.net_leased_area
        prj_data[bldg_name]['TotalVolumeAir'] = bldg.volume
        # prj_data[bldg_name]['YearOfConstruction'] = bldg.year_of_construction
        prj_data[bldg_name]['InnerWallArea'] = bldg.inner_area
        # if bldg.type_of_building:
        #     prj_data[bldg_name]['TypeOfBuilding'] = bldg.type_of_building
        # todo use bldg.*_names if existing
        prj_data[bldg_name]['FloorHeight'] = bldg.height_of_floors
        prj_data[bldg_name]['NumberOfFloors'] = bldg.number_of_floors

        prj_data[bldg_name]['OuterWallArea'] = {}
        outer_wall_area_total = 0
        for orient in bldg.outer_area:
            # some archetypes use floats, some integers for orientation in
            # TEASER
            orient = float(orient)
            if orient == -1:
                prj_data[bldg_name]['RoofArea'] += bldg.outer_area[orient]
            elif orient == -2:
                prj_data[bldg_name]['GroundFloorArea'] += bldg.outer_area[orient]
            else:
                if orient not in \
                        prj_data[bldg_name]['OuterWallArea']:
                    prj_data[bldg_name]['OuterWallArea'][orient] = 0
                prj_data[bldg_name]['OuterWallArea'][orient] += \
                    bldg.outer_area[orient]
                outer_wall_area_total += bldg.outer_area[orient]
        window_area_total = 0
        prj_data[bldg_name]['WindowArea'] = {}
        for orient in bldg.window_area:
            orient = float(orient)
            if orient not in prj_data[bldg_name]['WindowArea']:
                prj_data[bldg_name]['WindowArea'][orient] = 0
            prj_data[bldg_name]['WindowArea'][orient] += \
                bldg.window_area[orient]
            window_area_total += bldg.window_area[orient]
        prj_data[bldg_name]['WindowArea_Total'] = window_area_total
        prj_data[bldg_name]['OuterWallArea_Total'] = outer_wall_area_total
        prj_data[bldg_name][
            'WindowWallRatio'] = window_area_total / outer_wall_area_total
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
            # u_values_win.append(tz.model_attr.u_value_win)
            # u_values_inner_wall.append(tz.model_attr.ua_value_iw/tz.model_attr.area_iw)
            # u_values_outer_wall.append(tz.model_attr.ua_value_ow/tz.model_attr.area_ow)
            # u_values_roof.append(tz.model_attr.ua_value_rt/tz.model_attr.area_rt)
            # u_values_ground_floor.append(tz.model_attr.ua_value_gf/tz.model_attr.area_gf)
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
            prj_data[bldg_name]['UValueOuterWall'] = sum(u_values_outer_wall) \
                                                     / len(u_values_outer_wall)
        else:
            prj_data[bldg_name]['UValueOuterWall'] = 0

        if len(u_values_inner_wall) > 0:
            prj_data[bldg_name]['UValueInnerWall'] = sum(u_values_inner_wall) \
                                                     / len(u_values_inner_wall)
        else:
            prj_data[bldg_name]['UValueInnerWall'] = 0

        if len(u_values_win) > 0:
            prj_data[bldg_name]['UValueWindow'] = sum(u_values_win) \
                                                  / len(u_values_win)
        else:
            prj_data[bldg_name]['UValueWindow'] = 0

        if len(u_values_door) > 0:
            prj_data[bldg_name]['UValueDoor'] = sum(u_values_door) \
                                                / len(u_values_door)
        else:
            prj_data[bldg_name]['UValueDoor'] = 0

        if len(u_values_roof) > 0:
            prj_data[bldg_name]['UValueRoof'] = sum(u_values_roof) \
                                                / len(u_values_roof)
        else:
            prj_data[bldg_name]['UValueRoof'] = 0

        if len(u_values_ceiling) > 0:
            prj_data[bldg_name]['UValueCeiling'] = sum(u_values_ceiling) \
                                                   / len(u_values_ceiling)
        else:
            prj_data[bldg_name]['UValueCeiling'] = 0

        if len(u_values_ground_floor) > 0:
            prj_data[bldg_name]['UValueGroundFloor'] = sum(
                u_values_ground_floor) \
                                                       / len(
                u_values_ground_floor)
        else:
            prj_data[bldg_name]['UValueGroundFloor'] = 0

        if len(g_values_windows) > 0:
            prj_data[bldg_name]['gValueWindow'] = sum(g_values_windows) \
                                                  / len(g_values_windows)
        else:
            prj_data[bldg_name]['gValueWindow'] = 0

    # flat the keys
        bldg_data = prj_data[bldg_name]
        prj_data_flat = {}
        for key, val in bldg_data.items():
            if isinstance(bldg_data[key], dict):
                for subkey in bldg_data[key].keys():
                    prj_data_flat[str(key) + '_' + f"{subkey:03}"] = bldg_data[key][
                        subkey]
            else:
                prj_data_flat[key] = bldg_data[key]

        bldg_add_list = {'OuterWall': [], 'Window': []}
        for key in prj_data_flat.keys():
            if key.startswith('OuterWallArea_'):
                bldg_add_list['OuterWall'].append(key)
            if key.startswith('WindowArea_'):
                bldg_add_list['Window'].append(key)
        bldg_add_list['OuterWall'].sort()
        bldg_add_list['Window'].sort()

        bldg_sorted_list = [
            'NetGroundArea',
            'nZones'
            'GroundFloorArea',
            'RoofArea',
            'FloorHeight',
            'NumberOfFloors',
            'TotalVolumeAir',
            *bldg_add_list['OuterWall'],
            *bldg_add_list['Window'],
            'WindowWallRatio',
            'InnerWallArea',
            'UValueOuterWall',
            'UValueInnerWall',
            'UValueWindow',
            'UValueDoor',
            'UValueRoof',
            'UValueCeiling',
            'UValueGroundFloor',
            'gValueWindow',

        ]
        # round values
        for key, value in prj_data_flat.items():
            prj_data_flat[key] = round(value, 2)

        bldg_data_flat_sorted = [(k, prj_data_flat[k]) for k in bldg_sorted_list if
                                k in prj_data_flat.keys()]

        # Draw an abstract image of the building and save it with plotly to HTML
        interactive_fig = create_house_wireframe(
            area_north=prj_data_flat["OuterWallArea_0.0"],
            area_east=prj_data_flat["OuterWallArea_90.0"],
            area_south=prj_data_flat["OuterWallArea_180.0"],
            area_west=prj_data_flat["OuterWallArea_270.0"],
            height=prj_data_flat["FloorHeight"],
            window_area_north=prj_data_flat["WindowArea_0.0"],
            window_area_east=prj_data_flat["WindowArea_90.0"],
            window_area_south=prj_data_flat["WindowArea_180.0"],
            window_area_west=prj_data_flat["WindowArea_270.0"],
            num_floors=prj_data_flat["NumberOfFloors"],
            roof_angle=30)
        html_filename_plotly =\
            f"D:/10_ProgramTesting/interactive_plot_{bldg_name}.html"
        interactive_fig.write_html(html_filename_plotly)

        keys = ['']
        keys.extend([x[0] for x in bldg_data_flat_sorted])

        values = ['TEASER']
        values.extend([x[1] for x in bldg_data_flat_sorted])

        output_name = 'teaser_data' if not name else name

        create_html_page(bldg_data_flat_sorted, bldg_name, html_filename_plotly)
        with open(os.path.join(path, '%s.csv' % output_name), 'w', newline='',
                  encoding='utf-8') as f:
            csvwriter = csv.writer(f, delimiter=';')
            csvwriter.writerow(keys)
            csvwriter.writerow(localize_floats(values))
    return bldg_data_flat_sorted


def create_html_page(prj_data_tuples, prj_name, iframe_src):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{html.escape(prj_name)} - Project Data</title>
        <style>
            .container {{
                display: flex;
                justify-content: space-between;
            }}
            .table-container {{
                width: 50%;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
            }}
            th, td {{
                padding: 8px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            h1 {{
                text-align: center;
            }}
            .section {{
                background-color: #f2f2f2;
                font-weight: bold;
            }}
            .iframe-container {{
                width: 50%;
                border: 1px solid #ddd;
            }}
            iframe {{
                width: 100%;
                height: 500px;
                border: none;
            }}
        </style>
    </head>
    <body>
        <h1>{html.escape(prj_name)} - Project Data</h1>
        <div class="container">
            <div class="table-container">
                <table>
                    <tr>
                        <th>Key</th>
                        <th>Value</th>
                    </tr>
    """

    current_category = None
    for key, value in prj_data_tuples:
        category = None

        # Handle category names
        if key.startswith("OuterWallArea_") or key.startswith("WindowArea_"):
            category = "Wall and Window Areas"
        elif key.startswith("UValue"):
            category = "U-Values"
        elif key == "OuterWallArea_Total":
            category = "Total Wall Area"
        elif key == "WindowArea_Total":
            category = "Total Window Area"
        elif key in ["NetGroundArea", "TotalVolumeAir"]:
            category = key.replace("TotalVolumeAir", "Total Volume of Air").replace("NetGroundArea", "Net Ground Area")

        if category and category != current_category:
            html_content += f"""
                <tr class="section">
                    <td colspan="2">{html.escape(category)}</td>
                </tr>
            """
            current_category = category

        # Split camel case key names into human-readable strings
        key_human_readable = ' '.join([word.capitalize() for word in key.split('_')])

        html_content += f"""
            <tr>
                <td>{html.escape(key_human_readable)}</td>
                <td>{html.escape(str(value))}</td>
            </tr>
        """

    html_content += f"""
                </table>
            </div>
            <div class="iframe-container">
                <iframe src="{iframe_src}"></iframe>
            </div>
        </div>
    </body>
    </html>
    """

    with open(f"D:/10_ProgramTesting/{prj_name}_project_data.html",
              "w") as html_file:
        html_file.write(html_content)


def create_house_wireframe(area_north, area_east, area_south, area_west, height, num_floors=1, roof_angle=30,
                           window_area_north=0, window_area_east=0, window_area_south=0, window_area_west=0):
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
            [vertices[0], vertices[1], vertices[2], vertices[3], vertices[0]],  # 0: bottom
            [vertices[4], vertices[5], vertices[6], vertices[7], vertices[4]],  # 1: top
            [vertices[0], vertices[1], vertices[5], vertices[4], vertices[0]],  # 2: south
            [vertices[2], vertices[3], vertices[7], vertices[6], vertices[2]],  # 3: north
            [vertices[1], vertices[2], vertices[6], vertices[5], vertices[1]],  # 4: east
            [vertices[4], vertices[7], vertices[3], vertices[0], vertices[4]],  # 5: west
        ]

        # Add walls as 3D polygons with color fill
        for edge in edges:
            xs, ys, zs = zip(*edge)
            fig.add_trace(go.Mesh3d(x=xs, y=ys, z=zs, i=[0, 0, 1, 0], j=[1, 2, 2, 3], k=[2, 3, 3, 1],
                                    opacity=0.25, color='gray'))

        # Fenster hinzufügen
        window_gap_top_bottom = 0.5
        for i, (window_area, wall_vertices) in enumerate(zip(
                [window_area_north, window_area_east, window_area_south, window_area_west],
                [edges[3], edges[4], edges[2], edges[5]])):
            num_windows_on_side = int(window_area / num_floors)
            window_height = height - window_gap_top_bottom
            window_width = window_area / (num_floors * window_height)
            window_x_center = wall_vertices[0][0] + (wall_vertices[1][0] - wall_vertices[0][0]) / 2
            window_y_center = wall_vertices[0][1] + (wall_vertices[2][1] - wall_vertices[0][1]) / 2
            window_z_center = floor_height + window_gap_top_bottom / 2 + window_height / 2

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






def create_3d_house_diagram(prj_data_tuples):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ground_floor_area = prj_data_tuples.get('GroundFloorArea', 0)
    outer_wall_areas = {
        angle: prj_data_tuples.get(f'OuterWallArea_{angle}', 0)
        for angle in [0, 90, 180, 270]
    }
    window_areas = {
        angle: prj_data_tuples.get(f'WindowArea_{angle}', 0)
        for angle in [0, 90, 180, 270]
    }
    roof_area = prj_data_tuples.get('RoofArea', 0)

    # Define vertices for the house
    vertices = np.array([
        [0, 0, 0],
        [0, ground_floor_area, 0],
        [ground_floor_area, ground_floor_area, 0],
        [ground_floor_area, 0, 0],
        [0, 0, roof_area],
        [0, ground_floor_area, roof_area],
        [ground_floor_area, ground_floor_area, roof_area],
        [ground_floor_area, 0, roof_area]
    ])

    # Define faces for the house
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[0], vertices[3], vertices[7], vertices[4]],
        [vertices[1], vertices[2], vertices[6], vertices[5]]
    ]

    # Draw the faces of the house
    ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='black', alpha=0.5))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_xlim(0, ground_floor_area * 1.5)
    ax.set_ylim(0, ground_floor_area * 1.5)
    ax.set_zlim(0, roof_area * 1.5)

    plt.show()
