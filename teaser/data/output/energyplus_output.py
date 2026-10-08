"""EnergyPlus input (IDF) of the AixLib high order archetype

Writes the building envelope of an AixLibHighOrderSingleFamilyHouse as an
EnergyPlus model, e.g. for BESMod's Spawn of EnergyPlus building: the
eleven zones of its 3D geometry (see aixlib_high_order.geometry) with the
archetype's own constructions and windows. Heating, internal gains and the
ventilation of the heated rooms are left to the tool driving the model, as
Spawn does from Modelica. Only the attic gets its air change, for when
EnergyPlus simulates it on its own; Spawn drops it for a zone that is
modelled in Modelica, as BESMod's attic is.

The constructions are TEASER's layers, turned to EnergyPlus' order from
outside to inside. The windows are simple glazing systems with the
window's U-value and, as the frame lets no solar radiation through, a
solar heat gain coefficient of g_value * (1 - frame_fraction).
"""

import os

from teaser.logic.archetypebuildings.aixlib_high_order.geometry import (
    building_geometry)
from teaser.logic.archetypebuildings.aixlib_high_order.singlefamilyhouse \
    import _ATTIC_AIR_CHANGE_RATES

IDF_VERSION = "24.2"


def _object(kind, *fields):
    """One IDF object, a field per line"""
    lines = [f"{kind},"]
    for i, value in enumerate(fields):
        if isinstance(value, float):
            value = f"{value:.10g}"
        lines.append(f"    {value}{';' if i == len(fields) - 1 else ','}")
    return "\n".join(lines) + "\n"


class _Constructions:
    """Collects the materials and constructions an IDF needs, once each"""

    def __init__(self):
        self.materials = {}
        self.constructions = {}
        self.glazings = {}

    def _material(self, layer):
        material = layer.material
        name = f"{material.name}_{layer.thickness * 1000:.1f}mm"
        properties = (
            "MediumRough", float(layer.thickness),
            float(material.thermal_conduc), float(material.density),
            float(material.heat_capac) * 1000,
            float(material.ir_emissivity or 0.9),
            float(material.solar_absorp or 0.7),
            float(material.solar_absorp or 0.7))
        if self.materials.setdefault(name, properties) != properties:
            raise ValueError(f"Two layers of {name} differ in their properties")
        return name

    def add(self, name, layers_inside_out):
        """A construction from layers listed from the zone outwards"""
        layers = [self._material(layer) for layer in reversed(layers_inside_out)]
        if self.constructions.setdefault(name, layers) != layers:
            raise ValueError(f"Construction {name} defined twice differently")
        return name

    def glazing(self, window):
        u_value = float(window.u_value)
        shgc = float(window.g_value) * (1 - float(window.frame_fraction))
        name = f"Glazing_U{u_value:.3f}_SHGC{shgc:.3f}"
        self.glazings[name] = (u_value, shgc, shgc)
        self.constructions.setdefault(name, [name])
        return name

    def objects(self):
        text = ""
        for name, (roughness, thickness, conductivity, density, specific_heat,
                   thermal, solar, visible) in self.materials.items():
            text += _object("Material", name, roughness, thickness,
                            conductivity, density, specific_heat, thermal,
                            solar, visible)
        for name, (u_value, shgc, visible) in self.glazings.items():
            text += _object("WindowMaterial:SimpleGlazingSystem", name,
                            u_value, shgc, visible)
        for name, layers in self.constructions.items():
            text += _object("Construction", name, *layers)
        return text


def _element_layers(bldg):
    """The layers of each element of the archetype, from its room outwards"""
    zone = bldg.thermal_zones[0]
    layers = {}
    for element in (zone.outer_walls + zone.rooftops + zone.ground_floors
                    + zone.inner_walls + zone.floors + zone.ceilings):
        layers[element.name] = list(element.layer)
    for room, elements in bldg.unheated_room_envelope_elements.items():
        for name, element in elements.items():
            layers[f"{room}_{name}"] = list(element.layer)
    # the ceilings towards the attic are not part of the zone, which only
    # has the stand-ins integrating the attic
    for room, elements in bldg.detailed_geo.items():
        for name, info in elements.items():
            adjacent = info.get("adjacent")
            if info["type"] == "Ceiling" and adjacent \
                    and adjacent[0] in bldg.unheated_room_envelope_elements:
                _, ceiling_layers, _ = bldg._ceiling_to_unheated_room(info)
                layers[f"{room}_{name}"] = list(ceiling_layers)
                layers[f"{adjacent[0]}_{adjacent[1]}"] = list(reversed(ceiling_layers))
    return layers


def _vertices(vertices):
    return [float(c) for point in vertices for c in point]


def export_idf(bldg, path, run_period_days=None, slab_thickness=0.3,
               attic_slab_thickness=0.3, timesteps_per_hour=12):
    """Writes the envelope of an AixLibHighOrderSingleFamilyHouse as IDF

    Parameters
    ----------
    bldg : AixLibHighOrderSingleFamilyHouse
        The archetype, calculated (calc_building_parameter), so that its
        elements carry their layers.
    path : str
        The IDF file to write.
    run_period_days : int
        Adds a run period over the first days of the year, to run the model
        in EnergyPlus alone. Spawn sets its own.
    slab_thickness, attic_slab_thickness : float [m]
        Gaps between the floors, see geometry.building_geometry.
    timesteps_per_hour : int
        EnergyPlus' zone time steps per hour, at which Spawn also couples
        it with Modelica. 12, as in BESMod's own Spawn model: with 6, the
        attic's air in Modelica, small next to its light uninsulated roof,
        became unstable.

    Returns
    -------
    path : str
    """
    zones = building_geometry(bldg, slab_thickness, attic_slab_thickness)
    element_layers = _element_layers(bldg)
    windows = {w.name: w for w in bldg.thermal_zones[0].windows}
    constructions = _Constructions()
    t_ground = float(bldg.thermal_zones[0].t_ground) - 273.15

    text = f"! EnergyPlus model of {bldg.name}, written by TEASER\n\n"
    text += _object("Version", IDF_VERSION)
    text += _object("SimulationControl", "No", "No", "No", "No",
                    "Yes" if run_period_days else "No", "No", 1)
    text += _object("Building", bldg.name, float(bldg.rotation), "Suburbs",
                    0.04, 0.4, "FullInteriorAndExterior", 25, 6)
    text += _object("Timestep", timesteps_per_hour)
    text += _object("SurfaceConvectionAlgorithm:Inside", "TARP")
    text += _object("SurfaceConvectionAlgorithm:Outside", "DOE-2")
    text += _object("Site:GroundTemperature:BuildingSurface", *[t_ground] * 12)
    if run_period_days:
        end = run_period_days
        text += _object("RunPeriod", "TEASER", 1, 1, "", 1 + (end - 1) // 31,
                        1 + (end - 1) % 31, "", "", "Yes", "Yes", "No", "Yes",
                        "Yes")
    text += _object("GlobalGeometryRules", "UpperLeftCorner",
                    "CounterClockWise", "Relative")

    surfaces_text = ""
    for name, zone in zones.items():
        text += _object("Zone", name, 0.0, 0.0, 0.0, 0.0, 1, 1, "autocalculate",
                        "autocalculate", "autocalculate", "", "",
                        "No" if name in bldg.unheated_room_envelope_elements
                        else "Yes")
        for surface in zone.surfaces:
            room, element = surface.element if surface.element else (None, None)
            if element is None:
                # a gap above the walls between the rooms below the attic:
                # the attic's floor construction there
                element = next(s.element[1] for s in zone.surfaces
                               if s.kind == surface.kind and s.element)
                room = name
            construction = constructions.add(f"{room}_{element}",
                                             element_layers[f"{room}_{element}"])
            exposed = "SunExposed" if surface.boundary == "Outdoors" else "NoSun"
            wind = "WindExposed" if surface.boundary == "Outdoors" else "NoWind"
            surfaces_text += _object(
                "BuildingSurface:Detailed", surface.name, surface.kind,
                construction, name, "", surface.boundary,
                surface.partner or "", exposed, wind, "autocalculate",
                len(surface.vertices), *_vertices(surface.vertices))
            for window in surface.windows:
                glazing = constructions.glazing(windows[window.name])
                surfaces_text += _object(
                    "FenestrationSurface:Detailed", window.name, "Window",
                    glazing, surface.name, "", "autocalculate", "", 1,
                    len(window.vertices), *_vertices(window.vertices))
    text += constructions.objects() + surfaces_text

    attic_air_change = bldg.attic_air_change_rate
    if attic_air_change is None:
        attic_air_change = _ATTIC_AIR_CHANGE_RATES[bldg.attic_infiltration_class]
    text += _object("ScheduleTypeLimits", "Fraction", 0.0, 1.0, "Continuous")
    text += _object("Schedule:Constant", "AlwaysOn", "Fraction", 1.0)
    for room in bldg.unheated_room_envelope_elements:
        text += _object("ZoneInfiltration:DesignFlowRate",
                        f"{room}_air_change", room, "AlwaysOn",
                        "AirChanges/Hour", "", "", "", float(attic_air_change),
                        1.0, 0.0, 0.0, 0.0)

    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as file:
        file.write(text)
    return path
