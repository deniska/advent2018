import sys
import collections

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve(points):
    min_x = min(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_x = max(p[0] for p in points) + 1
    max_y = max(p[1] for p in points) + 1
    infpoints = set()
    c = collections.Counter()
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            p = (x, y)
            closest = sorted(points, key=lambda point: dist(p, point))
            if dist(closest[0], p) == dist(closest[1], p):
                continue
            if x in (min_x, max_x) or y in (min_y, max_y):
                infpoints.add(closest[0])
            c[closest[0]] += 1
    for p, d in c.most_common():
        if p in infpoints:
            continue
        return d

def solve2(points):
    min_x = min(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_x = max(p[0] for p in points) + 1
    max_y = max(p[1] for p in points) + 1
    c = 0
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            p = (x, y)
            if sum(dist(p, point) for point in points) < 10000:
                c += 1
    return c


def main(argv):
    fname = 'input06.txt'
    if len(argv) > 1:
        fname = argv[1]
    points = []
    with open(fname) as f:
        for line in f:
            a, b = line.strip().split(', ')
            points.append((int(a), int(b)))
    print(solve(points))
    print(solve2(points))

if __name__ == '__main__':
    main(sys.argv)
