"""Three-dimensional geometry of the detailed multi family house archetype

The floor plan is Kühn/Nikolowski's two-flat module: a staircase in the
middle of the building's north side with a flat on either side of it, the
east one mirroring the west one. Each flat has six rooms, in three rows from
south to north:

- Living | Bedroom, the bedroom reaching to the module's axis behind the
  staircase,
- Children (over two rows) | Hallway,
- Children | Bath | Kitchen | half the staircase.

The module repeats along the building's length (number_of_staircases) and
the storeys stack on top of each other (number_of_floors), over an unheated
basement and below an unheated attic with a gable roof. Each staircase is a
single zone over all storeys.

Coordinates are in m, x to the east, y to the north and z upwards, for the
building unrotated (its rotation is left to the tool, e.g. EnergyPlus' north
axis), with the origin at the outer corner of the south-west walls. All
zones are boxes with the rooms' inner dimensions, except the attic, so
neighbouring zones are separated by gaps as thick as the wall or slab
between them. Two faces facing each other across such a gap share a surface
over their overlap; whatever of a face is left over is either part of the
building's envelope or faces a gap where walls meet, which is adiabatic.
"""

from dataclasses import dataclass, field, replace
from math import tan, pi

import numpy as np

from teaser.logic.archetypebuildings.aixlib_high_order.geometry import (
    Surface, Window, Zone, _normal, _outward)

_TOLERANCE = 1e-9

# The rooms of a flat, (u0, u1, v0, v1) in the flat's own plan coordinates
# are given by _flat_rooms
ROOM_TYPES = ("Living", "Bedroom", "Children", "Hallway", "Bath", "Kitchen")

# Kühn/Nikolowski's windows per room: (width, height, sill) in m, the
# Living room's first one being the balcony door, which sits 1 cm above the
# floor, as EnergyPlus wants a window inside its wall, not on its edge. Each
# room has them on its one facade, the Living room and the Bedroom on the
# south, the others on the north side.
_WINDOWS = {
    "Living": ((1.125, 2.125, 0.01), (1.125, 1.25, 0.875)),
    "Bedroom": ((2.25, 1.25, 0.875),),
    "Children": ((1.25, 1.25, 0.875),),
    "Bath": ((0.875, 1.25, 0.875),),
    "Kitchen": ((1.125, 1.25, 0.875),),
    "Hallway": (),
}
# the staircase's window on each storey, in its north facade
_STAIRCASE_WINDOW = (1.875, 1.25, 0.875)


@dataclass
class Plan:
    """Dimensions of Kühn/Nikolowski's floor plan, unscaled [m]

    The room widths are along x (the building's length), the row depths
    along y. widths_scale and depths_scale stretch the rooms, but not the
    staircase or the walls.
    """
    thickness_outer_wall: float = 0.32
    thickness_inner_wall: float = 0.17
    staircase_width: float = 2.60
    depth_living_row: float = 4.30
    depth_hallway_row: float = 1.66
    depth_north_row: float = 3.06
    width_living: float = 4.25
    width_bedroom: float = 3.675
    width_children: float = 2.62
    width_bath: float = 1.50
    width_kitchen: float = 2.25
    room_height: float = 2.5
    slab_thickness: float = 0.21
    basement_height: float = 2.5
    widths_scale: float = 1.0
    depths_scale: float = 1.0

    def scaled(self, widths_scale, depths_scale):
        return replace(self, widths_scale=widths_scale,
                       depths_scale=depths_scale)

    @property
    def half_module(self):
        """Inner length of a flat up to the module's axis [m]"""
        s = self.widths_scale
        return ((self.width_children + self.width_bath + self.width_kitchen) * s
                + 3 * self.thickness_inner_wall + self.staircase_width / 2)

    @property
    def inner_depth(self):
        return ((self.depth_living_row + self.depth_hallway_row
                 + self.depth_north_row) * self.depths_scale
                + 2 * self.thickness_inner_wall)

    @property
    def storey_height(self):
        return self.room_height + self.slab_thickness


def _flat_rooms(plan):
    """The rooms of the west flat of a module, {type: (u0, u1, v0, v1)}

    u runs east from the module's west inner face, v north from the south
    inner face.
    """
    s, d = plan.widths_scale, plan.depths_scale
    t = plan.thickness_inner_wall
    c, b, k = (plan.width_children * s, plan.width_bath * s,
               plan.width_kitchen * s)
    d1, d2, d3 = (plan.depth_living_row * d, plan.depth_hallway_row * d,
                  plan.depth_north_row * d)
    half = plan.half_module
    # the living row ends at the axis, in the middle of the wall between
    # the two bedrooms, and keeps the plan's ratio of its two rooms
    living_row = half - 1.5 * t
    living = living_row * plan.width_living / (plan.width_living
                                               + plan.width_bedroom)
    v_hall = d1 + t
    v_north = v_hall + d2 + t
    v_end = v_north + d3
    return {
        "Living": (0.0, living, 0.0, d1),
        "Bedroom": (living + t, half - t / 2, 0.0, d1),
        "Children": (0.0, c, v_hall, v_end),
        "Hallway": (c + t, c + 2 * t + b + k, v_hall, v_hall + d2),
        "Bath": (c + t, c + t + b, v_north, v_end),
        "Kitchen": (c + 2 * t + b, c + 2 * t + b + k, v_north, v_end),
    }


def flat_area(plan):
    """Net floor area of one flat [m2]"""
    return sum((u1 - u0) * (v1 - v0)
               for u0, u1, v0, v1 in _flat_rooms(plan).values())


def scale_plan(plan, net_leased_area_per_flat, scaling="length"):
    """The plan scaled so a flat has net_leased_area_per_flat

    Parameters
    ----------
    scaling : str
        "length" stretches the rooms along the building's length only, as
        Kühn/Nikolowski's larger variant does, keeping the depth of the
        building. "proportional" stretches them along both.
    """
    if scaling not in ("length", "proportional"):
        raise ValueError(f"Unknown scaling {scaling!r}, use 'length' or "
                         f"'proportional'.")

    def area(factor):
        return flat_area(plan.scaled(
            factor, factor if scaling == "proportional" else 1.0))

    low, high = 1e-3, 1.0
    while area(high) < net_leased_area_per_flat:
        high *= 2
    if area(low) > net_leased_area_per_flat:
        raise ValueError(
            f"A flat can not be smaller than {area(low):.1f} m2.")
    for _ in range(200):
        middle = (low + high) / 2
        if area(middle) < net_leased_area_per_flat:
            low = middle
        else:
            high = middle
    factor = (low + high) / 2
    return plan.scaled(factor, factor if scaling == "proportional" else 1.0)


@dataclass
class ZoneInfo:
    """What a zone of the geometry is

    kind is "room", "staircase", "basement" or "attic". Rooms belong to a
    flat (numbered from 1, west to east) on a storey (0 = ground floor),
    staircases to a module (from 1).
    """
    name: str
    kind: str
    heated: bool
    storey: int = None
    flat: int = None
    module: int = None
    room_type: str = None
    box: tuple = None


@dataclass
class Geometry:
    """The zones of the building and what they are"""
    zones: dict
    info: dict
    plan: Plan
    length: float
    depth: float
    number_of_floors: int
    number_of_staircases: int
    roof_tilt: float
    neighbours: tuple

    @property
    def heated_rooms(self):
        return [name for name, info in self.info.items() if info.heated]


def room_name(storey, flat, room_type):
    return f"F{storey}_A{flat}_{room_type}"


@dataclass
class _Face:
    """A rectangular face of a zone, perpendicular to axis

    sign is the direction of its outward normal along axis, coord its
    position on it and (u0, u1, v0, v1) its extent along the two other axes,
    in the order x, y, z.
    """
    zone: str
    axis: int
    sign: int
    coord: float
    rect: tuple
    pieces: list = field(default_factory=list)

    @property
    def tag(self):
        return {(0, -1): "W", (0, 1): "E", (1, -1): "S", (1, 1): "N",
                (2, -1): "floor", (2, 1): "ceiling"}[(self.axis, self.sign)]

    def vertices(self, rect):
        u0, u1, v0, v1 = rect
        others = [a for a in range(3) if a != self.axis]
        points = []
        for u, v in ((u0, v0), (u1, v0), (u1, v1), (u0, v1)):
            point = [0.0, 0.0, 0.0]
            point[self.axis] = self.coord
            point[others[0]], point[others[1]] = u, v
            points.append(point)
        inside = [0.0, 0.0, 0.0]
        inside[self.axis] = self.coord - self.sign
        inside[others[0]], inside[others[1]] = (u0 + u1) / 2, (v0 + v1) / 2
        return _outward(points, np.array(inside))


def _box_faces(name, box):
    x0, x1, y0, y1, z0, z1 = box
    bounds = ((x0, x1), (y0, y1), (z0, z1))
    faces = []
    for axis in range(3):
        others = [bounds[a] for a in range(3) if a != axis]
        rect = (*others[0], *others[1])
        faces.append(_Face(name, axis, -1, bounds[axis][0], rect))
        faces.append(_Face(name, axis, 1, bounds[axis][1], rect))
    return faces


def _overlap(a, b):
    u0, u1 = max(a[0], b[0]), min(a[1], b[1])
    v0, v1 = max(a[2], b[2]), min(a[3], b[3])
    if u1 - u0 > _TOLERANCE and v1 - v0 > _TOLERANCE:
        return (u0, u1, v0, v1)
    return None


def _leftover(rect, covered):
    """The parts of rect not covered by the rectangles covered, as few
    rectangles as a row-wise merge of the grid gives"""
    us = sorted({rect[0], rect[1]} | {c for r in covered for c in r[:2]
                                       if rect[0] < c < rect[1]})
    vs = sorted({rect[2], rect[3]} | {c for r in covered for c in r[2:]
                                       if rect[2] < c < rect[3]})

    def free(u0, u1, v0, v1):
        um, vm = (u0 + u1) / 2, (v0 + v1) / 2
        return not any(r[0] < um < r[1] and r[2] < vm < r[3] for r in covered)

    rows = []
    for v0, v1 in zip(vs[:-1], vs[1:]):
        runs, start = [], None
        for u0, u1 in zip(us[:-1], us[1:]):
            if free(u0, u1, v0, v1):
                start = u0 if start is None else start
                end = u1
            elif start is not None:
                runs.append((start, end))
                start = None
        if start is not None:
            runs.append((start, end))
        rows.append(((v0, v1), runs))
    pieces = []
    open_runs = {}
    for (v0, v1), runs in rows:
        still_open = {}
        for run in runs:
            if run in open_runs:
                still_open[run] = (open_runs[run][0], v1)
            else:
                still_open[run] = (v0, v1)
        for run, (a, b) in open_runs.items():
            if run not in still_open:
                pieces.append((*run, a, b))
        open_runs = still_open
    pieces += [(*run, a, b) for run, (a, b) in open_runs.items()]
    return [p for p in pieces if p[1] - p[0] > _TOLERANCE
            and p[3] - p[2] > _TOLERANCE]


def building_geometry(plan=None, number_of_floors=5, number_of_staircases=1,
                      roof_tilt=30.0, neighbours=0):
    """Builds the zones of the multi family house

    Parameters
    ----------
    plan : Plan
        The floor plan's dimensions, already scaled (see scale_plan).
    number_of_floors : int
        Heated storeys, each with two flats per staircase.
    number_of_staircases : int
        Modules of a staircase with a flat on either side, side by side
        along the building's length.
    roof_tilt : float [deg]
        Tilt of the two halves of the gable roof, with its ridge along the
        building's length.
    neighbours : int or tuple
        Buildings adjoining the gable walls, which are then adiabatic: 0, 1
        (on the west side), 2, or a tuple of "west" and/or "east".

    Returns
    -------
    Geometry
    """
    plan = plan or Plan()
    if isinstance(neighbours, int):
        neighbours = {0: (), 1: ("west",), 2: ("west", "east")}[neighbours]
    neighbours = tuple(neighbours)
    if set(neighbours) - {"west", "east"}:
        raise ValueError(f"Unknown neighbours {neighbours}")
    if number_of_floors < 1 or number_of_staircases < 1:
        raise ValueError("The building needs at least one storey and one "
                         "staircase.")

    t_out, t_in = plan.thickness_outer_wall, plan.thickness_inner_wall
    half = plan.half_module
    module_length = 2 * half
    inner_length = (number_of_staircases * module_length
                    + (number_of_staircases - 1) * t_in)
    length = inner_length + 2 * t_out
    depth = plan.inner_depth + 2 * t_out
    x_env, y_env = (t_out, length - t_out), (t_out, depth - t_out)

    z_floor = [plan.basement_height + plan.slab_thickness
               + storey * plan.storey_height
               for storey in range(number_of_floors)]
    z_attic = z_floor[-1] + plan.room_height + plan.slab_thickness

    boxes, info = {}, {}
    windows = []  # (zone, axis, sign, rect)
    flat_rooms = _flat_rooms(plan)
    v_hall = flat_rooms["Hallway"][2]
    v_end = flat_rooms["Kitchen"][3]
    for module in range(number_of_staircases):
        x_module = t_out + module * (module_length + t_in)
        for side in (0, 1):
            flat_index = 2 * module + side
            for storey in range(number_of_floors):
                z0 = z_floor[storey]
                for room_type, (u0, u1, v0, v1) in flat_rooms.items():
                    if side == 1:
                        u0, u1 = module_length - u1, module_length - u0
                    box = (x_module + u0, x_module + u1, t_out + v0,
                           t_out + v1, z0, z0 + plan.room_height)
                    name = room_name(storey, flat_index + 1, room_type)
                    boxes[name] = box
                    info[name] = ZoneInfo(name, "room", True, storey,
                                          flat_index + 1, module + 1,
                                          room_type, box)
                    facade = _WINDOWS[room_type]
                    if not facade:
                        continue
                    south = room_type in ("Living", "Bedroom")
                    y = box[2] if south else box[3]
                    width = box[1] - box[0]
                    for i, (w, h, sill) in enumerate(facade):
                        w *= plan.widths_scale
                        centre = box[0] + (i + 0.5) * width / len(facade)
                        windows.append((name, 1, -1 if south else 1,
                                        (centre - w / 2, centre + w / 2,
                                         z0 + sill, z0 + sill + h)))
        name = f"Staircase{module + 1}"
        box = (x_module + half - plan.staircase_width / 2,
               x_module + half + plan.staircase_width / 2,
               t_out + v_hall, t_out + v_end,
               z_floor[0], z_floor[-1] + plan.room_height)
        boxes[name] = box
        info[name] = ZoneInfo(name, "staircase", False, module=module + 1,
                              box=box)
        w, h, sill = _STAIRCASE_WINDOW
        centre = (box[0] + box[1]) / 2
        for z0 in z_floor:
            windows.append((name, 1, 1, (centre - w / 2, centre + w / 2,
                                         z0 + sill, z0 + sill + h)))
    boxes["Basement"] = (*x_env, *y_env, 0.0, plan.basement_height)
    info["Basement"] = ZoneInfo("Basement", "basement", False,
                                box=boxes["Basement"])
    info["Attic"] = ZoneInfo("Attic", "attic", False)

    faces = [face for name, box in boxes.items()
             for face in _box_faces(name, box)]
    attic_floor = _Face("Attic", 2, -1, z_attic, (*x_env, *y_env))
    faces.append(attic_floor)

    # the faces facing each other across a wall or slab share their overlap
    gap = max(t_in, plan.slab_thickness) + 1e-6
    by_direction = {}
    for face in faces:
        by_direction.setdefault((face.axis, face.sign), []).append(face)
    pairs = []
    for axis in range(3):
        for low in by_direction.get((axis, 1), []):
            for high in by_direction.get((axis, -1), []):
                distance = high.coord - low.coord
                if not _TOLERANCE < distance <= gap:
                    continue
                rect = _overlap(low.rect, high.rect)
                if rect is not None:
                    pairs.append((low, high, rect))

    zones = {name: Zone(name) for name in info}
    names = {}

    def surface_name(face, partner):
        base = f"{face.zone}_{face.tag}" + (f"_{partner}" if partner else "")
        count = names.get(base, 0)
        names[base] = count + 1
        return base if count == 0 else f"{base}_{count}"

    for low, high, rect in pairs:
        low_name = surface_name(low, high.zone)
        high_name = surface_name(high, low.zone)
        low.pieces.append(rect)
        high.pieces.append(rect)
        zones[low.zone].surfaces.append(Surface(
            low_name, _kind(low), low.vertices(rect), "Surface",
            (low.zone, high.zone), high_name))
        zones[high.zone].surfaces.append(Surface(
            high_name, _kind(high), high.vertices(rect), "Surface",
            (high.zone, low.zone), low_name))

    for face in faces:
        boundary, what = _envelope_boundary(face, x_env, y_env, neighbours,
                                            info)
        for rect in _leftover(face.rect, face.pieces):
            surface = Surface(surface_name(face, None), _kind(face),
                              face.vertices(rect), boundary,
                              (face.zone, what))
            zones[face.zone].surfaces.append(surface)

    _attic_envelope(zones["Attic"], x_env, y_env, z_attic, roof_tilt,
                    neighbours)

    for index, (zone, axis, sign, rect) in enumerate(windows):
        _place_window(zones[zone], axis, sign, rect,
                      f"{zone}_win{sum(1 for w in windows[:index] if w[0] == zone)}")

    return Geometry(zones, info, plan, length, depth, number_of_floors,
                    number_of_staircases, roof_tilt, neighbours)


def _kind(face):
    if face.axis < 2:
        return "Wall"
    return "Floor" if face.sign < 0 else "Ceiling"


def _envelope_boundary(face, x_env, y_env, neighbours, info):
    """Boundary condition of what is left of a face after its neighbours

    Returns the boundary and what the surface faces: None for the outside
    or the ground, "neighbour" for an adjoining building and "gap" for the
    walls or slabs between the zones.
    """
    on_envelope = (
        (face.axis == 0 and abs(face.coord - x_env[0 if face.sign < 0 else 1])
         < 1e-6)
        or (face.axis == 1 and abs(face.coord - y_env[0 if face.sign < 0 else 1])
            < 1e-6)
        or (face.axis == 2 and face.sign < 0 and face.zone == "Basement"))
    if not on_envelope:
        return "Adiabatic", "gap"
    if face.axis == 0 and ("west" if face.sign < 0 else "east") in neighbours:
        return "Adiabatic", "neighbour"
    return ("Ground" if info[face.zone].kind == "basement" else "Outdoors",
            None)


def _attic_envelope(zone, x_env, y_env, z_attic, roof_tilt, neighbours):
    """The attic's two roof halves and its two gable walls"""
    (x0, x1), (y0, y1) = x_env, y_env
    y_ridge = (y0 + y1) / 2
    z_ridge = z_attic + (y1 - y0) / 2 * tan(roof_tilt * pi / 180)
    inside = np.array([(x0 + x1) / 2, y_ridge, (z_attic + z_ridge) / 2])
    zone.surfaces.append(Surface(
        "Attic_roof_S", "Roof",
        _outward([(x0, y0, z_attic), (x1, y0, z_attic), (x1, y_ridge, z_ridge),
                  (x0, y_ridge, z_ridge)], inside), "Outdoors",
        ("Attic", None)))
    zone.surfaces.append(Surface(
        "Attic_roof_N", "Roof",
        _outward([(x0, y1, z_attic), (x1, y1, z_attic), (x1, y_ridge, z_ridge),
                  (x0, y_ridge, z_ridge)], inside), "Outdoors",
        ("Attic", None)))
    for x, side, tag in ((x0, "west", "W"), (x1, "east", "E")):
        zone.surfaces.append(Surface(
            f"Attic_{tag}", "Wall",
            _outward([(x, y0, z_attic), (x, y1, z_attic), (x, y_ridge, z_ridge)],
                     inside),
            "Adiabatic" if side in neighbours else "Outdoors",
            ("Attic", "neighbour" if side in neighbours else None)))


def _place_window(zone, axis, sign, rect, name):
    """Puts a window into the outdoor surface of zone that contains it"""
    u0, u1, v0, v1 = rect
    for surface in zone.surfaces:
        if surface.boundary != "Outdoors" or surface.kind != "Wall":
            continue
        normal = surface.normal
        if abs(normal[axis] - sign) > 1e-6:
            continue
        others = [a for a in range(3) if a != axis]
        p = surface.vertices
        lo = p[:, others].min(axis=0)
        hi = p[:, others].max(axis=0)
        if (lo[0] - 1e-9 <= u0 and u1 <= hi[0] + 1e-9
                and lo[1] - 1e-9 <= v0 and v1 <= hi[1] + 1e-9):
            coord = p[0, axis]
            points = []
            for u, v in ((u0, v0), (u1, v0), (u1, v1), (u0, v1)):
                point = [0.0, 0.0, 0.0]
                point[axis] = coord
                point[others[0]], point[others[1]] = u, v
                points.append(point)
            vertices = np.array(points, dtype=float)
            if np.dot(_normal(vertices), normal) < 0:
                vertices = vertices[::-1]
            surface.windows.append(Window(name, vertices, (zone.name, None)))
            return
    raise ValueError(f"The window {name} fits into no outer wall of "
                     f"{zone.name}.")
