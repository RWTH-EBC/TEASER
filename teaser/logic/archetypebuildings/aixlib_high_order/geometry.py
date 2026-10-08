"""Three-dimensional geometry of the AixLib high order archetype

Builds the rooms of AixLibHighOrderSingleFamilyHouse as closed polyhedra,
for building simulation tools that need surfaces with vertices, such as
EnergyPlus. The geometry is AixLib's one family dwelling (OFD) with the
archetype's scaled dimensions (top_level_geo_params) and matches its inner
dimensions: every heated room has the floor area, volume and element areas
the archetype gives it, and the surfaces carry the names of its elements.

Coordinates are in m, x to the east, y to the north and z upwards, for the
archetype unrotated (its rotation is left to the tool, e.g. EnergyPlus'
north axis). The building's long side runs from west to east, and AixLib's
floor plan has two strips along it, of room_width each:

- south strip: Livingroom | Kitchen, upstairs Bedroom | Children2
- north strip: Hobby | Corridor_gf | WC_Storage, upstairs Children1 |
  Corridor_upp | Bath

The upper floor's rooms are AixLib's: an outer wall of room_height_short,
the roof sloping up at roof_tilt and a flat ceiling of room_width_short,
below the attic. Every zone is therefore a cross section in the y-z plane
extruded along x.

As AixLib's walls have a thickness, the rooms are separated by gaps: one
thickness_iw_simple between the rooms and between the two strips, as the
archetype takes it for the attic's width, and slab_thickness and
attic_slab_thickness between the floors. Where a wall faces the gap
between two rooms rather than a room, that part is adiabatic.

The attic spans the whole length of the rooms below it, so it is
2 * thickness_iw_simple longer than the archetype's roof_length, which the
archetype takes for its roof areas and volume.
"""

from dataclasses import dataclass, field
from math import tan, pi

import numpy as np

# The rooms of each strip from west to east, as (ground floor, upper floor)
_SOUTH = (("Livingroom", "Bedroom"), ("Kitchen", "Children2"))
_NORTH = (("Hobby", "Children1"), ("Corridor_gf", "Corridor_upp"),
          ("WC_Storage", "Bath"))

# TEASER's orientation of a face's outward normal, 0 = north, clockwise
_ORIENTATIONS = {(0, -1): 180, (0, 1): 0, (-1, 0): 270, (1, 0): 90}

_TOLERANCE = 1e-9


@dataclass
class Window:
    """A window in a surface, vertices counter-clockwise seen from outside"""
    name: str
    vertices: np.ndarray
    element: tuple

    @property
    def area(self):
        return _area(self.vertices)

    @property
    def normal(self):
        return _normal(self.vertices)


@dataclass
class Surface:
    """One planar surface of a zone

    vertices are counter-clockwise seen from outside the zone, so the
    normal points out of it. boundary is "Outdoors", "Ground", "Surface"
    (towards the surface named partner) or "Adiabatic". element is the
    archetype's (room, element name) the surface belongs to, or None for
    the parts facing a gap between rooms that the archetype has no element
    for.
    """
    name: str
    kind: str
    vertices: np.ndarray
    boundary: str
    element: tuple = None
    partner: str = None
    windows: list = field(default_factory=list)

    @property
    def area(self):
        """Gross area, including the windows"""
        return _area(self.vertices)

    @property
    def net_area(self):
        return self.area - sum(window.area for window in self.windows)

    @property
    def normal(self):
        return _normal(self.vertices)

    @property
    def tilt(self):
        return float(np.degrees(np.arccos(np.clip(self.normal[2], -1, 1))))

    @property
    def orientation(self):
        """TEASER's orientation: 0 = north clockwise, -1 up, -2 down"""
        normal = self.normal
        if abs(normal[0]) < 1e-6 and abs(normal[1]) < 1e-6:
            return -1 if normal[2] > 0 else -2
        return float(np.degrees(np.arctan2(normal[0], normal[1])) % 360)


@dataclass
class Zone:
    name: str
    surfaces: list = field(default_factory=list)

    @property
    def volume(self):
        """Volume enclosed by the surfaces (divergence theorem)"""
        volume = 0.0
        for surface in self.surfaces:
            p = surface.vertices
            for i in range(1, len(p) - 1):
                volume += np.dot(p[0], np.cross(p[i], p[i + 1])) / 6
        return volume

    @property
    def floor_area(self):
        return sum(s.area for s in self.surfaces if s.kind == "Floor")


def _normal(p):
    n = np.zeros(3)
    for i in range(len(p)):
        n += np.cross(p[i], p[(i + 1) % len(p)])
    return n / np.linalg.norm(n)


def _area(p):
    n = np.zeros(3)
    for i in range(len(p)):
        n += np.cross(p[i], p[(i + 1) % len(p)])
    return float(np.linalg.norm(n) / 2)


def _outward(vertices, inside):
    """Orders the vertices counter-clockwise seen from outside, i.e. with
    the normal pointing away from the point inside the zone"""
    vertices = np.asarray(vertices, dtype=float)
    if np.dot(_normal(vertices), vertices.mean(axis=0) - inside) < 0:
        vertices = vertices[::-1]
    return vertices


class _Prism:
    """A zone's cross section in the y-z plane, extruded from x0 to x1"""

    def __init__(self, x0, x1, profile):
        self.x0, self.x1 = x0, x1
        self.profile = [tuple(point) for point in profile]
        centre = np.mean(self.profile, axis=0)
        self.inside = np.array([(x0 + x1) / 2, centre[0], centre[1]])

    def end(self, x):
        return _outward([(x, y, z) for y, z in self.profile], self.inside)

    def edges(self):
        n = len(self.profile)
        return [(self.profile[i], self.profile[(i + 1) % n]) for i in range(n)]

    def side(self, edge, x0=None, x1=None):
        (ya, za), (yb, zb) = edge
        x0 = self.x0 if x0 is None else x0
        x1 = self.x1 if x1 is None else x1
        return _outward([(x0, ya, za), (x1, ya, za), (x1, yb, zb),
                         (x0, yb, zb)], self.inside)


def _split(interval, neighbours):
    """Splits interval (x0, x1) by the neighbours' intervals

    Returns (x0, x1, neighbour or None) pieces, None where no neighbour
    faces that part.
    """
    x0, x1 = interval
    cuts = {x0, x1}
    for (a, b), _ in neighbours:
        cuts.update(c for c in (a, b) if x0 < c < x1)
    cuts = sorted(cuts)
    pieces = []
    for a, b in zip(cuts[:-1], cuts[1:]):
        if b - a < _TOLERANCE:
            continue
        middle = (a + b) / 2
        owner = next((name for (c, d), name in neighbours
                      if c - _TOLERANCE <= middle <= d + _TOLERANCE), None)
        pieces.append((a, b, owner))
    return pieces


def _element(bldg, room, kind, orientation=None, neighbour=None):
    """Name of the archetype's element of room a surface belongs to"""
    elements = bldg.detailed_geo[room]
    candidates = []
    for name, info in elements.items():
        if kind == "Floor" and info["type"] not in ("Floor", "GroundFloor"):
            continue
        if kind == "Ceiling" and info["type"] != "Ceiling":
            continue
        if kind == "Roof" and info["type"] != "Roof":
            continue
        if kind == "Wall":
            if info["type"] not in ("OuterWall", "InnerWall"):
                continue
            # inner walls are found by their neighbour, outer walls by
            # their orientation
            if neighbour is None and abs(info["ori"] - orientation) > 1e-6:
                continue
        if kind == "Roof" and orientation is not None and \
                abs(info["ori"] - orientation) > 1e-6:
            continue
        adjacent = info.get("adjacent")
        if neighbour is not None and (adjacent is None
                                      or adjacent[0] != neighbour):
            continue
        if neighbour is None and kind == "Wall" and adjacent is not None:
            continue
        candidates.append(name)
    if len(candidates) != 1:
        raise ValueError(
            f"No unique element of {room} for a {kind} towards "
            f"{neighbour or 'the outside'} (orientation {orientation}): "
            f"{candidates}")
    return candidates[0]


def _extent(uv, v):
    """The u range of the convex polygon uv at the height v"""
    us = []
    for (ua, va), (ub, vb) in zip(uv, np.roll(uv, -1, axis=0)):
        if min(va, vb) - 1e-9 <= v <= max(va, vb) + 1e-9:
            if abs(vb - va) < 1e-12:
                us += [ua, ub]
            else:
                us.append(ua + (v - va) / (vb - va) * (ub - ua))
    return (min(us), max(us)) if us else (0.0, 0.0)


def _windows(bldg, room, element, surface, sill=0.9, margin=0.1,
             height=1.4):
    """The window of an element in its surface

    The window is a rectangle as close to height high as its area and the
    surface allow, kept margin off the surface's edges. In walls its sill
    is at sill, lowered if needed, and it is centred where the wall is high
    enough, e.g. below the flat ceiling in the upper floor's gable walls.
    In roofs it is centred, height long along the slope.
    """
    info = bldg.detailed_geo[room][element]
    if not info.get("with_window"):
        return []
    area = info["windowarea"]
    p = surface.vertices
    normal = surface.normal
    vertical = abs(normal[2]) < 1e-6
    if vertical:
        u_axis = np.array([-normal[1], normal[0], 0.0])
        v_axis = np.array([0.0, 0.0, 1.0])
    else:
        u_axis = np.array([1.0, 0.0, 0.0])
        v_axis = np.cross(normal, u_axis)
        v_axis /= np.linalg.norm(v_axis)
        if v_axis[2] < 0:
            v_axis = -v_axis
    origin = p[0]
    uv = np.array([[np.dot(q - origin, u_axis), np.dot(q - origin, v_axis)]
                   for q in p])
    v_min, v_max = uv[:, 1].min(), uv[:, 1].max()

    best = None
    for window_height in np.linspace(0.5, v_max - v_min - 2 * margin, 200):
        bottoms = ([v_min + min(sill, v_max - v_min - margin - window_height)]
                   if vertical else
                   [(v_min + v_max - window_height) / 2])
        if vertical:
            bottoms += list(np.linspace(v_min + margin, bottoms[0], 20))
        for bottom in bottoms:
            top = bottom + window_height
            if bottom < v_min + margin - 1e-9 or top > v_max - margin + 1e-9:
                continue
            # the polygon is convex, so it is narrowest at either edge
            low, high = _extent(uv, bottom), _extent(uv, top)
            u0, u1 = max(low[0], high[0]) + margin, min(low[1], high[1]) - margin
            if u1 - u0 + 1e-9 < area / window_height:
                continue
            score = (abs(window_height - height), abs(bottom - bottoms[0]))
            if best is None or score < best[0]:
                best = (score, window_height, bottom, (u0 + u1) / 2)
            break
    if best is None:
        raise ValueError(
            f"The window of {room} {element} ({area:.2f} m2) does not fit "
            f"into its surface.")
    _, window_height, v0, u_centre = best
    window_width = area / window_height
    u0 = u_centre - window_width / 2
    corners = [(u0, v0), (u0 + window_width, v0),
               (u0 + window_width, v0 + window_height),
               (u0, v0 + window_height)]
    vertices = np.array([origin + u * u_axis + v * v_axis for u, v in corners])
    if np.dot(_normal(vertices), normal) < 0:
        vertices = vertices[::-1]
    return [Window(f"{room}_{element}_win", vertices, (room, element))]


def building_geometry(bldg, slab_thickness=0.3, attic_slab_thickness=0.3):
    """Builds the zones of an AixLibHighOrderSingleFamilyHouse

    Parameters
    ----------
    bldg : AixLibHighOrderSingleFamilyHouse
        The archetype, generated (its top_level_geo_params and detailed_geo
        are read).
    slab_thickness : float [m]
        Gap between the ground and the upper floor.
    attic_slab_thickness : float [m]
        Gap between the upper floor's ceilings and the attic.

    Returns
    -------
    zones : dict
        Zone by room name, the ten heated rooms and the "Attic".
    """
    geo = bldg.top_level_geo_params
    width = geo["room_width"]
    t = geo["thickness_iw_simple"]
    h = geo["height_of_floors"]
    h_short = geo["room_height_short"]
    w_short = geo["room_width_short"]
    tilt = geo["roof_tilt"] * pi / 180
    lengths = {"Livingroom": geo["room1_length"], "Kitchen": geo["room5_length"],
               "Hobby": geo["l1"], "Corridor_gf": geo["room3_length"],
               "WC_Storage": geo["l4"]}
    z_upper = h + slab_thickness
    z_attic = z_upper + h + attic_slab_thickness

    # x intervals of the rooms, with one gap between neighbours
    intervals = {}
    for strip in (_SOUTH, _NORTH):
        x = 0.0
        for ground, upper in strip:
            intervals[ground] = intervals[upper] = (x, x + lengths[ground])
            x += lengths[ground] + t
    total_length = x - t
    strips = {"south": (0.0, width), "north": (width + t, 2 * width + t)}
    strip_of = {room: name for name, rooms in (("south", _SOUTH),
                                               ("north", _NORTH))
                for pair in rooms for room in pair}

    prisms = {}
    for strip in (_SOUTH, _NORTH):
        for ground, upper in strip:
            y0, y1 = strips[strip_of[ground]]
            prisms[ground] = _Prism(*intervals[ground],
                                    [(y0, 0), (y1, 0), (y1, h), (y0, h)])
            if strip_of[upper] == "south":
                # outer wall at y0, ceiling towards the middle at y1
                y_ceiling = y1 - w_short
                profile = [(y0, z_upper), (y1, z_upper), (y1, z_upper + h),
                           (y_ceiling, z_upper + h), (y0, z_upper + h_short)]
            else:
                y_ceiling = y0 + w_short
                profile = [(y0, z_upper), (y1, z_upper),
                           (y1, z_upper + h_short), (y_ceiling, z_upper + h),
                           (y0, z_upper + h)]
            prisms[upper] = _Prism(*intervals[upper], profile)
    y_attic = (width - w_short, width + t + w_short)
    ridge = (y_attic[1] - y_attic[0]) / 2 * tan(tilt)
    prisms["Attic"] = _Prism(0.0, total_length,
                             [(y_attic[0], z_attic), (y_attic[1], z_attic),
                              ((y_attic[0] + y_attic[1]) / 2, z_attic + ridge)])

    zones = {name: Zone(name) for name in prisms}
    upper_of = {g: u for strip in (_SOUTH, _NORTH) for g, u in strip}
    ground_of = {u: g for g, u in upper_of.items()}

    def add(room, kind, vertices, boundary, element=None, partner=None,
            name=None):
        surface = Surface(name or f"{room}_{element}", kind, vertices,
                          boundary, (room, element) if element else None,
                          partner)
        if element and boundary == "Outdoors":
            surface.windows = _windows(bldg, room, element, surface)
        zones[room].surfaces.append(surface)
        return surface

    def neighbours_along_x(room, strip_rooms):
        """The rooms west and east of room in its strip and floor"""
        ordered = [r for r in strip_rooms]
        i = ordered.index(room)
        return (ordered[i - 1] if i > 0 else None,
                ordered[i + 1] if i < len(ordered) - 1 else None)

    for floor in (0, 1):
        for strip, other in ((_SOUTH, _NORTH), (_NORTH, _SOUTH)):
            rooms = [pair[floor] for pair in strip]
            facing = [pair[floor] for pair in other]
            for room in rooms:
                prism = prisms[room]
                west, east = neighbours_along_x(room, rooms)
                for x, side, neighbour in ((prism.x0, 270, west),
                                           (prism.x1, 90, east)):
                    element = _element(bldg, room, "Wall", side, neighbour)
                    add(room, "Wall", prism.end(x),
                        "Surface" if neighbour else "Outdoors", element,
                        f"{neighbour}_{_element(bldg, neighbour, 'Wall', (side + 180) % 360, room)}"
                        if neighbour else None)
                for edge in prism.edges():
                    (ya, za), (yb, zb) = edge
                    if abs(za - zb) < _TOLERANCE and abs(ya - yb) > _TOLERANCE:
                        bottom = za < prism.inside[2]
                        if bottom:
                            if floor == 0:
                                add(room, "Floor", prism.side(edge), "Ground",
                                    _element(bldg, room, "Floor"))
                            else:
                                below = ground_of[room]
                                add(room, "Floor", prism.side(edge), "Surface",
                                    _element(bldg, room, "Floor"),
                                    f"{below}_{_element(bldg, below, 'Ceiling')}")
                        elif floor == 0:
                            above = upper_of[room]
                            add(room, "Ceiling", prism.side(edge), "Surface",
                                _element(bldg, room, "Ceiling"),
                                f"{above}_{_element(bldg, above, 'Floor')}")
                        else:
                            element = _element(bldg, room, "Ceiling")
                            add(room, "Ceiling", prism.side(edge), "Surface",
                                element, f"Attic_{bldg.detailed_geo[room][element]['adjacent'][1]}")
                    elif abs(ya - yb) < _TOLERANCE:
                        outer = abs(ya) < _TOLERANCE or \
                            abs(ya - (2 * width + t)) < _TOLERANCE
                        orientation = 180 if strip is _SOUTH else 0
                        if outer:
                            add(room, "Wall", prism.side(edge), "Outdoors",
                                _element(bldg, room, "Wall", orientation))
                            continue
                        orientation = (orientation + 180) % 360
                        pieces = _split((prism.x0, prism.x1),
                                        [(intervals[r], r) for r in facing])
                        _add_split_wall(bldg, room, prism, edge, pieces,
                                        orientation, add)
                    else:
                        orientation = 180 if strip is _SOUTH else 0
                        add(room, "Roof", prism.side(edge), "Outdoors",
                            _element(bldg, room, "Roof", orientation))

    attic = prisms["Attic"]
    ceilings = []
    for room in (pair[1] for strip in (_SOUTH, _NORTH) for pair in strip):
        element = _element(bldg, room, "Ceiling")
        ceilings.append((room, bldg.detailed_geo[room][element]["adjacent"][1],
                         element))
    for edge in attic.edges():
        (ya, za), (yb, zb) = edge
        if abs(za - zb) < _TOLERANCE:
            # the floor: the ceilings of the five rooms below, and the
            # strips above the walls between them
            for strip_name, (y0, y1) in (("south", (y_attic[0], width)),
                                         ("north", (width + t, y_attic[1]))):
                rooms = [(r, e, c) for r, e, c in ceilings
                         if strip_of[r] == strip_name]
                pieces = _split((0.0, total_length),
                                [(intervals[r], (r, e, c)) for r, e, c in rooms])
                for i, (x0, x1, owner) in enumerate(pieces):
                    vertices = _outward([(x0, y0, z_attic), (x1, y0, z_attic),
                                         (x1, y1, z_attic), (x0, y1, z_attic)],
                                        attic.inside)
                    if owner is None:
                        add("Attic", "Floor", vertices, "Adiabatic",
                            name=f"Attic_floor_gap_{strip_name}_{i}")
                    else:
                        room, element, ceiling = owner
                        add("Attic", "Floor", vertices, "Surface", element,
                            f"{room}_{ceiling}")
            # and the strip above the load-bearing wall between the strips
            vertices = _outward([(0, width, z_attic),
                                 (total_length, width, z_attic),
                                 (total_length, width + t, z_attic),
                                 (0, width + t, z_attic)], attic.inside)
            add("Attic", "Floor", vertices, "Adiabatic",
                name="Attic_floor_gap_middle")
        else:
            vertices = attic.side(edge)
            orientation = _ORIENTATIONS[(0, int(np.sign(_normal(vertices)[1])))]
            add("Attic", "Roof", vertices, "Outdoors",
                _element(bldg, "Attic", "Roof", orientation))
    for x, side in ((attic.x0, 270), (attic.x1, 90)):
        add("Attic", "Wall", attic.end(x), "Outdoors",
            _element(bldg, "Attic", "Wall", side))
    return zones


def _add_split_wall(bldg, room, prism, edge, pieces, orientation, add):
    """The wall towards the other strip, split by the rooms behind it

    Each part facing a room gets that room's element and pairs with the
    matching part of its wall. A part facing the gap between two rooms is
    adiabatic and joins the element whose area the archetype gives it,
    i.e. the one still short of its area.
    """
    targets = {}
    for x0, x1, neighbour in pieces:
        if neighbour is not None:
            element = _element(bldg, room, "Wall", orientation, neighbour)
            targets[element] = bldg.detailed_geo[room][element]["area"]
    gathered = {element: 0.0 for element in targets}
    pending = []
    for index, (x0, x1, neighbour) in enumerate(pieces):
        vertices = prism.side(edge, x0, x1)
        if neighbour is None:
            pending.append((index, vertices))
            continue
        element = _element(bldg, room, "Wall", orientation, neighbour)
        back = _element(bldg, neighbour, "Wall", (orientation + 180) % 360,
                        room)
        surface = add(room, "Wall", vertices, "Surface", element,
                      f"{neighbour}_{back}_{room}",
                      name=f"{room}_{element}_{neighbour}")
        gathered[element] += surface.area
    for index, vertices in pending:
        area = _area(vertices)
        element = min(targets, key=lambda e: abs(targets[e] - gathered[e] - area))
        gathered[element] += area
        add(room, "Wall", vertices, "Adiabatic", element,
            name=f"{room}_{element}_gap{index}")
