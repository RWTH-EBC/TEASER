"""holds functions to create a report for a TEASER project model"""

orient_mapper = {
    0: 'North',
    90: 'East',
    180: 'South',
    270: 'West'
}
def localize_floats(row):
    return [
        str(el).replace('.', ',') if isinstance(el, float) else el
        for el in row
    ]

def calc_report_data(prj, path):
    prj_data = {}
    for bldg in prj.buildings:
        bldg_name = bldg.name
        prj_data[bldg_name] = {}
        # prj_data[bldg_name]['CalculatedHeatLoad'] = bldg.sum_heat_load
        # prj_data[bldg_name]['CalculatedCoolingLoad'] = bldg.sum_cooling_load
        prj_data[bldg_name]['NetGroundArea'] = bldg.net_leased_area
        prj_data[bldg_name]['TotalVolumeAir'] = bldg.volume
        # prj_data[bldg_name]['YearOfConstruction'] = bldg.year_of_construction
        prj_data[bldg_name]['InnerWallArea'] = bldg.inner_area
        # if bldg.type_of_building:
        #     prj_data[bldg_name]['TypeOfBuilding'] = bldg.type_of_building
        # todo use bldg.*_names if existing

        prj_data[bldg_name]['OuterWallArea'] = {}
        outer_wall_area_total = 0
        for orient in bldg.outer_area:
            if orient == -1:
                prj_data[bldg_name]['RoofArea'] = bldg.outer_area[orient]
            elif orient == -2:
                prj_data[bldg_name]['GroundFloorArea'] = bldg.outer_area[orient]
            else:
                prj_data[bldg_name]['OuterWallArea'][orient_mapper[orient]] = \
                    bldg.outer_area[orient]
                outer_wall_area_total += bldg.outer_area[orient]
        window_area_total = 0
        prj_data[bldg_name]['WindowArea'] = {}
        for orient in bldg.window_area:
            prj_data[bldg_name]['WindowArea'][orient_mapper[orient]] = \
                bldg.window_area[orient]
            window_area_total += bldg.window_area[orient]
        prj_data[bldg_name]['WindowArea_Total'] = window_area_total
        prj_data[bldg_name]['OuterWallArea_Total'] = outer_wall_area_total
        prj_data[bldg_name]['WindowWallRatio'] = window_area_total / outer_wall_area_total
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
            for door in tz.doors:
                u_values_door.append(
                    1 / (door.r_conduc * door.area))
        if len(u_values_outer_wall) > 0:
            prj_data[bldg_name]['UValueOuterWall'] = sum(u_values_outer_wall)\
                                                 /len(u_values_outer_wall)
        else:
            prj_data[bldg_name]['UValueOuterWall'] = 0

        if len(u_values_inner_wall) > 0:
            prj_data[bldg_name]['UValueInnerWall'] = sum(u_values_inner_wall)\
                                                 /len(u_values_inner_wall)
        else:
            prj_data[bldg_name]['UValueInnerWall'] = 0

        if len(u_values_win)>0:
            prj_data[bldg_name]['UValueWindow'] = sum(u_values_win)\
                                                 /len(u_values_win)
        else:
            prj_data[bldg_name]['UValueWindow'] = 0

        if len(u_values_door)>0:
            prj_data[bldg_name]['UValueDoor'] = sum(u_values_door)\
                                                /len(u_values_door)
        else:
            prj_data[bldg_name]['UValueDoor'] = 0

        if len(u_values_roof) > 0:
            prj_data[bldg_name]['UValueRoof'] = sum(u_values_roof)\
                                                 /len(u_values_roof)
        else:
            prj_data[bldg_name]['UValueRoof'] = 0

        if len(u_values_ceiling) > 0:
            prj_data[bldg_name]['UValueCeiling'] = sum(u_values_ceiling)\
                                                 /len(u_values_ceiling)
        else:
            prj_data[bldg_name]['UValueCeiling'] = 0

        if len(u_values_ground_floor) > 0:
            prj_data[bldg_name]['UValueGroundFloor'] = sum(u_values_ground_floor)\
                                                         /len(u_values_ground_floor)
        else:
            prj_data[bldg_name]['UValueGroundFloor'] = 0

        if len(g_values_windows) > 0:
            prj_data[bldg_name]['gValueWindow'] = sum(g_values_windows)\
                                                         /len(g_values_windows)
        else:
            prj_data[bldg_name]['gValueWindow'] = 0


        # flat the keys
    prj_data = prj_data[bldg_name]
    prj_data_flat = {}
    for key, val in prj_data.items():
        if isinstance(prj_data[key], dict):
            for subkey in prj_data[key].keys():
                prj_data_flat[str(key)+'_'+str(subkey)] = prj_data[key][subkey]
        else:
            prj_data_flat[key] = prj_data[key]



    prj_sorted_list = [
        'NetGroundArea',
        'OuterWallArea_Total',
        'OuterWallArea_South',
        'OuterWallArea_West',
        'OuterWallArea_North',
        'OuterWallArea_East',
        'RoofArea',
        'TotalVolumeAir',
        'InnerWallArea',
        'WindowArea_Total',
        'WindowArea_South',
        'WindowArea_North',
        'WindowArea_West',
        'WindowArea_East',
        'WindowWallRatio',
        'UValueOuterWall',
        'UValueInnerWall',
        'UValueWindow',
        'UValueDoor',
        'UValueRoof',
        'UValueCeiling',
        'UValueGroundFloor',
        'gValueWindow',
        'GroundFloorArea',
        'nZones'
    ]


    prj_data_flat_sorted = [(k, prj_data_flat[k]) for k in prj_sorted_list]
    keys = ['']
    keys.extend([x[0] for x in prj_data_flat_sorted])

    values = ['TEASER']
    values.extend([x[1] for x in prj_data_flat_sorted])
    import csv
    import os
    with open(os.path.join(path, 'teaser_data.csv'), 'w', newline='', encoding='utf-8') as f:
        csvwriter = csv.writer(f, delimiter=';')
        csvwriter.writerow(keys)
        csvwriter.writerow(localize_floats(values))
    return prj_data_flat_sorted
