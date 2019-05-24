import sys
import math
import networkx as nx

class CombatEnd(Exception):
    pass

adjacent = ((0, -1), (-1, 0), (1, 0), (0, 1))
def adjacent_coords(x, y):
    return [(x+dx, y+dy) for (dx, dy) in adjacent]

class Unit:

    def __init__(self, x, y, t, ap=3):
        self.t = t
        self.x = x
        self.y = y
        self.hp = 200
        self.ap = ap
        self.alive = True

    def move(self, units, walls):
        #print(self)
        adj = adjacent_coords(self.x, self.y)
        targets = [u for u in units if (u.t != self.t and u.alive)]
        if not targets:
            raise CombatEnd
        coords = units_to_coord(units)
        in_range = set()
        to_attack = []
        for t in targets:
            if (t.x, t.y) in adj:
                to_attack.append(t)
            for x, y in adjacent_coords(t.x, t.y):
                if (x, y) not in walls and (x, y) not in coords:
                    in_range.add((x, y))
        if to_attack:
            return
        #print_map(walls, units, {(self.x, self.y): self.t.lower(),
                                    #**{c: '?' for c in in_range}})
        reachable = self.reachable(coords, walls)

        in_range = {c for c in in_range if c in reachable}
        #print_map(walls, units, {c: '!' for c in in_range})

        size_x, size_y = max(walls)
        graph = nx.generators.grid_graph([size_y+1, size_x+1])
        for w in walls:
            graph.remove_node(w)
        for c, u in coords.items():
            if u is self:
                continue
            graph.remove_node(c)

        nearest_dist = math.inf
        nearest = None
        for c in in_range:
            d = nx.algorithms.shortest_path_length(graph, (self.x, self.y), c)
            if d < nearest_dist:
                nearest_dist = d
                nearest = set((c,))
            elif d == nearest_dist:
                nearest.add(c)
        if nearest is None:
            return # waiting turn
        chosen = min(nearest, key = lambda t: (t[1], t[0]))
        #print_map(walls, units, {chosen: '+'})
        graph.remove_node((self.x, self.y))
        min_coord = None
        min_coord_dist = math.inf
        for c in adjacent_coords(self.x, self.y):
            if c in walls or c in coords:
                continue
            try:
                l = nx.algorithms.shortest_path_length(graph, c, chosen)
            except nx.exception.NetworkXNoPath:
                continue
            if l < min_coord_dist:
                min_coord_dist = l
                min_coord = c
        self.x, self.y = min_coord

    def attack(self, units, part2 = False):
        targets = [u for u in units if u.t != self.t and u.alive]
        adj = adjacent_coords(self.x, self.y)
        nearby = []
        for t in targets:
            if (t.x, t.y) in adj:
                nearby.append(t)
        if not nearby:
            return
        target = min(nearby, key=lambda t: t.hp)
        target.hp -= self.ap
        if target.hp <= 0:
            if part2 and target.t == 'E':
                raise CombatEnd
            target.hp = 0
            target.alive = False

    def reachable(self, unit_coords, walls):
        to_check = adjacent_coords(self.x, self.y)
        reachable = set()
        seen = set()
        while to_check:
            coords = to_check.pop()
            if coords in seen:
                continue
            seen.add(coords)
            if coords in unit_coords or coords in walls:
                continue
            reachable.add(coords)
            for x, y in adjacent_coords(*coords):
                if (x, y) not in seen:
                    to_check.append((x, y))
        return reachable

    def __repr__(self):
        return f'<{self.t}({self.hp}): {self.x}, {self.y}>'

def unit_order(units):
    return [u for u in sorted(units, key=lambda u: (u.y, u.x)) if u.alive]

def units_to_coord(units):
    return {(u.x, u.y): u for u in units if u.alive}

def print_map(walls, units, override=None):
    return
    if override is None:
        override = {}
    size_x, size_y = max(walls)
    coords = units_to_coord(units)
    f = []
    for y in range(size_y+1):
        units_in_line = []
        for x in range(size_x+1):
            if (x, y) in walls:
                c = '#'
            else:
                c = '.'
            u = coords.get((x, y))
            if u is not None:
                c = u.t
                units_in_line.append(u)
            c = override.get((x, y), c)
            f.append(c)
        f.append(' ')
        f.append(', '.join(str(u) for u in units_in_line))
        f.append('\n')
    print(''.join(f))

def part1(argv):
    with open(argv[1]) as f:
        field = f.read()
    units = []
    walls = set()
    for y, line in enumerate(field.split('\n')):
        for x, c in enumerate(line):
            if c in ('G', 'E'):
                units.append(Unit(x, y, c))
            elif c == '#':
                walls.add((x, y))
    size_x, size_y = max(walls)
    field = field.replace('G', '.').replace('E', '.')
    print(units)
    print(field)
    rounds = 0
    while True:
        print_map(walls, units)
        units = unit_order(units)
        print('Rounds', rounds)
        for unit in units:
            if not unit.alive:
                continue
            try:
                t = unit.move(units, walls)
            except CombatEnd:
                print_map(walls, units)
                print(units)
                print(rounds * sum(u.hp for u in units if u.alive))
                return
            unit.attack(units)
        rounds += 1

def part2_iter(field, elf_ap):
    units = []
    walls = set()
    for y, line in enumerate(field.split('\n')):
        for x, c in enumerate(line):
            if c == 'E':
                units.append(Unit(x, y, c, elf_ap))
            elif c == 'G':
                units.append(Unit(x, y, c))
            elif c == '#':
                walls.add((x, y))
    size_x, size_y = max(walls)
    field = field.replace('G', '.').replace('E', '.')
    print(units)
    print(field)
    rounds = 0
    while True:
        print_map(walls, units)
        units = unit_order(units)
        print(f'Rounds: {rounds}; elf atk: {elf_ap}')
        for unit in units:
            if not unit.alive:
                continue
            try:
                t = unit.move(units, walls)
            except CombatEnd:
                print_map(walls, units)
                print(units)
                print(rounds * sum(u.hp for u in units if u.alive))
                return True
            try:
                unit.attack(units, True)
            except CombatEnd:
                return False
        rounds += 1

def part2(argv):
    with open(argv[1]) as f:
        field = f.read()
    elf_ap = 4
    while not part2_iter(field, elf_ap):
        elf_ap += 1

if __name__ == '__main__':
    part1(sys.argv)
    part2(sys.argv)
