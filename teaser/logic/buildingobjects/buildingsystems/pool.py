# created November 2022
# by TEASER4 Development Team

"""This module includes a class for pools
"""
import random
import math

import pandas as pd
from itertools import cycle, islice


class Pool(object):
    """Pool Class

    This class holds information for a pool.
    This class is very AixLib specific and holds some parameters that are only
    applicable to AixLib pool model.

    Parameters
    ----------
    parent : ThermalZone()
        The parent class of this object, the ThermalZone the pool belongs to.
        Allows for better control of hierarchical structures.
        Default is None.

    Attributes
    ----------
    pool_type : str
        pool type for the calulation of attributes, currently the following are supported:
        'Swimmer_pool', 'Nonswimmer_pool', 'Multipurpose_pool', 'Child_pool', 'Diving_pool','Freeform_pool'
    internal_id : float
        Random id for the distinction between different pools.
    name : str
        Individual name.
    area : float [m2]
        Pool area.
    width : float [m]
        Pool width.
    length : float [m]
        Pool length
    perimeter : float [m]
        Perimeter of pool [m]
    volume : float [m3]
        Pool volume.
    depth : float [m]
        Average pool depth.
    temperature : float [K]
        Pool temperature.
    temperature_air : float [K]
        Air temperature.
    filter_type : str
        Information on used filter type within the water treatment system.
        Possible input: '"Activated carbon filter with ozone', 'Two-layer filter with ozone',
        'Open quick filter', 'Closed quick filter', 'Closed sorption filter', 'Open suction filter',
        '"Quantozone filter', 'Quartz gravel filter', 'Two-layer filter'
    filter_combination : str
        Information on used filter combination within the water treatment system.
        Possible input: 'without_ozone', 'with_ozone', 'with_bromine', 'with_ultrafiltration'
    water_type : str
        Information on water usage within the pool.
        Possible inputs: 'Fresh water" or any other
    volume_flow : float [m3/h]
        Volume flow of water treatment according to DIN 19643-1"
    volume_flow_night : float [m3/h]
        Volume flow of water treatment at night according to DIN 19643-1
    use_partial_load : Boolean
        If true, the volume flow of the water treatment is reduced at night.
    volume_storage : float [m3]
        Volume of the water storage within the water treatment system according to DIN 19643-1
    beta_in_use : float [-]
        Factor for the evaporation within a used pool according to VDI 2089
    use_ideal_heat_exchanger : Boolean
        If true, the exported AixLib model includes an ideally heated pool.
    dp_heat_exchanger : float [Pa]
        pressure loss of heat exchanger, only needed if use_ideal_heat_exchanger = False.
    use_heat_recovery : Boolean
        If true, heat recovery is considered for waste water.
    eta_heat_recovery : float [-]
        Efficiency for heat recovery.
    use_pool_cover: Boolean
        If true, pool has a pool cover, which is used during night.
    use_wave_pool : Boolean
        If true, pool is realised with a wave machine, which is run regular.
    wave_height : float [m]
        Hight of produced waves.
    wave_width: float [m]
        Width of produced waves.
    wave_period : float [sec]
        Length of wave cycling period (wave production and break).
    wave_period_start : float [sec]
        Start time of first wave cycle.
    wave_share_period : float [-]
        Share of the time with wave generation within the cycling period.
    use_water_recycling : Boolean
        If true, water recycling unit within the water treatment system
    x_recycling : float [-]
        Rate of water recycling
    num_visitors : float [1/h]
        Average number of visitors per hour.
    num_filter_rinses : float [1/week]
       Required number of filter rinses per week according to DIN 19643-1
    m_flow_waste_water : float [kg/s]
        Water exchange due to filter rinses per week or people in the pool, DIN 19643-1
    area_pool_wall_inner : float [m2]
        Area of pool walls which is connected to inner rooms (inner pool walls).
    area_pool_wall_exterior : float [m2]
        Area of pool walls which is connected to the ground (pool wall with earth contact).
    area_pool_floor_inner : float [m2]
        Area of pool floor which is connected to inner rooms (inner pool floor).
    area_pool_floor_exterior : float [m2]
        Area of pool floor which is connected to the ground (pool floor with earth contact).
    h_con_water_horizontal : float [W/(m2*K)]
        Mean value for the heat transfer coefficient of free convection on horizontal pool floors.
    h_con_water_vertical : float [W/(m2*K)]
        Mean value for the heat transfer coefficient of free convection on vertical pool walls.
    pool_wall_construction_type : str
        Construction type of pool wall, supported construction types: 'concrete_with_insulation', 'stainless_steel'
    m_flow_evap_pool_used : float [kg/h]
        Evaporation mass flow of used pool with maximal occupancy
    """

    def __init__(self, parent=None):
        """Constructor of Pool Class, default values for swimmer pool
        """
        self.parent = parent
        self.pool_type = None
        self.name = None
        self.internal_id = random.random()
        self.area = None
        self.width = None
        self.length = None
        self.perimeter = None
        self.volume = None
        self.depth = None
        self.temperature = None
        self.temperature_air = 303.15+2
        self.filter_type = 'Open suction filter'
        self.filter_combination = 'without_ozone'
        self.water_type = 'Fresh water'
        self.volume_flow = None
        self.volume_flow_night = None
        self.use_partial_load = True
        self.volume_storage = None
        self.beta_in_use = None
        self.use_ideal_heat_exchanger = True
        self.dp_heat_exchanger = 350
        self.use_heat_recovery = True
        self.eta_heat_recovery = 0.8
        self.use_pool_cover = False
        self.use_wave_pool = False
        self.wave_height = 0
        self.wave_width = 0
        self.wave_period = 1800
        self.wave_period_start = 600
        self.wave_share_period = 10/30*100
        self.use_water_recycling = False
        self.x_recycling = 0.8
        self.num_visitors = None
        self.num_filter_rinses = 2
        self.m_flow_waste_water = None
        self.area_pool_wall_inner = None
        self.area_pool_wall_exterior = None
        self.area_pool_floor_inner = None
        self.area_pool_floor_exterior = None
        self.h_con_water_horizontal = 50.0
        self.h_con_water_vertical = 5200.0
        self.pool_wall_construction_type = 'concrete_with_insulation'
        self.m_flow_evap_pool_used = 0

    @property
    def parent(self):
        return self.parent

    @parent.setter
    def parent(self, value):
        if value is not None:
            ass_error_1 = "Parent has to be an instance of ThermalZone()"
            assert type(value).__name__ == "ThermalZone", ass_error_1
            self._parent = value
            self._parent.pools.append(self)
        else:
            self._parent = None


    def calc_pool_parameters(self):
        # Typical temperatures and depths for pools according to DIN 19643 and VDI 2089
        if self.pool_type == 'Swimmer_pool':
            self.depth = 2.5
            self.temperature = 301.15
        elif self.pool_type == 'Nonswimmer_pool':
            self.depth = 0.975
            self.temperature = 303.15
        elif self.pool_type == 'Child_pool':
            self.depth = 0.6
            self.temperature = 305.15
        elif self.pool_type == 'Multipurpose_pool':
            self.depth = 1.35
            self.temperature = 301.15
        elif self.pool_type == 'Diving_pool':
            self.depth = 3.8
            self.temperature = 301.15
        elif self.pool_type == 'Freeform_pool':
            self.depth = 0.75
            self.temperature = 303.15
        else:
            raise ValueError(f"Unknown pool type: {self.pool_type}. Only the following pool types are supported: " \
                        f"'Swimmer_pool', 'Nonswimmer_pool', 'Multipurpose_pool', 'Child_pool'," \
                        f" 'Multipurpose_pool', 'Diving_pool', 'Freeform_pool'")

        self.volume = self.area * self.depth

        # avereage number of visitors KOK
        self.num_visitors = round(self.area ** 0.58, 0)

        # Calculation of the nominal volume_flow according to DIN 19643-1
        # help parameter k
        if self.filter_combination == 'without_ozone' or \
                self.filter_combination == 'with_bromine':
            k = 0.5
        elif self.filter_combination == 'with_ozone':
            k = 0.6
        elif self.filter_combination == 'with_ultrafiltration':
            k = 1
        else:
            raise ValueError(f"Unknown filter combination: {self.filter_combination}. "
                             f"Only the following filter combinations are supported: "
                             f"'without_ozone', 'with_ozone', 'with_bromine', 'with_ultrafiltration' ")

        # help parameters m, a, n ; nominal load N
        if self.pool_type == 'Swimmer_pool' or self.pool_type == 'Diving_pool':
            a = 4.5
            n = 1
            m = None
            N = self.area * n/a
        elif self.pool_type == 'Nonswimmer_pool'\
                or self.pool_type == 'Freeform_pool' \
                or self.pool_type == 'Multipurpose_pool':
            a = 2.7
            n = 1
            m = None
            N = self.area * n / a
        elif self.pool_type == 'Child_pool':
            a = None
            n = None
            m = 2
            N = self.area * m * k
        else:
            raise ValueError(f"Unknown pool type: {self.pool_type}. Only the following pool types are supported: " \
                        f"'Swimmer_pool', 'Nonswimmer_pool', 'Multipurpose_pool', 'Child_pool'," \
                        f" 'Multipurpose_pool', 'Diving_pool', 'Freeform_pool'")

        # V_H: hygienic minimum volume flow
        # V_K: hygienic minimum volume flow for children pool
        # V_B: hydraulic minimum volume flow
        V_H = N / k          # Ratio of nominal load divided by factor k
        V_B = 1 * self.perimeter
        if self.pool_type == 'Child_pool' and self.area < 20:
            V_K = m * self.volume
        else:
            V_K = 0

        # volume_flow in m3/h
        if self.perimeter > 40:
            self.volume_flow = max(V_B, V_H) / 3600
        elif V_K > 0:
            self.volume_flow = min(V_H, V_K, V_B) / 3600
        else:
            self.volume_flow = min(V_H, V_B) / 3600

        # volume_flow_night
        if V_B > 30:
            self.volume_flow_night = V_B/3600
        else:
            self.volume_flow_night = 30/3600

        # volume_storage
        # help parameter v_f
        if self.filter_type == 'Activated carbon filter with ozone' \
            or self.filter_type == 'Two-layer filter with ozone':
            v_f = 50
        elif self.filter_type == 'Open quick filter':
            v_f = 15
        elif self.filter_type == 'Closed quick filter' \
            or self.filter_type == 'Closed sorption filter' \
            or self.filter_type == 'Open suction filter' \
            or self.filter_type == 'Quantozone filter' \
            or self.filter_type == 'Quartz gravel filter' \
            or self.filter_type == 'Two-layer filter':
            if self.water_type == 'Fresh water':
                v_f = 30/3600
            else:
                v_f = 20/3600
        else:
            raise ValueError(f"Unknown filter type: {self.filter_type}. "
                             f"Only the following filter types are supported: "
                             f"'Activated carbon filter with ozone','Two-layer filter with ozone',"
                             f"'Open quick filter','Closed quick filter','Closed sorption filter',"
                             f"'Quantozone filter','Quartz gravel filter','Two-layer filter'")

        # help parameter a_filter
        a_filter = self.volume_flow / v_f

        # help parameter V_v
        if a is not None:
            V_v = 0.075 * self.area / a
        else:
            V_v = None

        # help parameter V_w
        V_w = 0.052 * self.area * 10**(-0.144 * self.volume_flow/self.perimeter)

        # help parameter V_fs
        V_fs = a_filter * 5

        # Calculation of volume_storage
        self.volume_storage = V_v + V_w + V_fs

        # Calculation of beta_in_use according to VDI 2089 in m/s
        if self.pool_type == 'Freeform_pool' or self.pool_type == 'Multipurpose_pool':
            self.beta_in_use = 40/3600
        else:
            if self.depth > 1.35:
                self.beta_in_use = 28/3600
            else:
                self.beta_in_use = 40/3600

        # Caluclation of m_flow_waste_water
        m_visitors = 0.03 * 995.65 * self.num_visitors * 1/(24*3600)
        m_filter = 995.65 * self.num_filter_rinses * V_fs * 1/(7*24*3600)
        self.m_flow_waste_water = max(m_visitors, m_filter)

        # Calculation of evaporation mass flow at maximal occupancy according to VDI 2089 in kg/h
        R_D = 461.52   # specific gas constant for steam
        aritmethic_temperature = (self.temperature + self.temperature_air) /2
        # saturation pressure in Pa
        p_sat_air_temp = self.calc_sat_pressure(self.temperature_air)
        p_sat_pool_temp = self.calc_sat_pressure(self.temperature)


        self.m_flow_evap_pool_used = -((self.beta_in_use*3600)/(R_D*aritmethic_temperature))* \
                                     (p_sat_pool_temp-p_sat_air_temp)*self.area
        print('self.m_flow_evap_pool_used',self.m_flow_evap_pool_used)

    def calc_sat_pressure(self, temp):
        log_pw = 10.79574 * (1.0 - 273.16 / temp) \
                 - 5.02800 * math.log10(temp / 273.16) \
                 + 1.50475E-4 * (1 - math.pow(10, (-8.2969 * (temp/ 273.16 - 1.0)))) + 0.42873E-3 * \
                 (math.pow(10, (+4.76955 * (1.0 - 273.16 / temp))) - 1) + 0.78614
        p_sat = math.pow(10, log_pw)*100
        return p_sat





