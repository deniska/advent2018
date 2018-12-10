import sys
import re

class Point:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def tick(self):
        self.x += self.vx
        self.y += self.vy

def solve(points):
    i = 0
    while True:
        i += 1
        for p in points:
            p.tick()
        max_x = max(p.x for p in points)
        min_x = min(p.x for p in points)
        max_y = max(p.y for p in points)
        min_y = min(p.y for p in points)
        if max_x - min_x < 70: # precisely arbitrary number
            print('X;Y')
            for p in points:
                print(f'{p.x};{p.y}')
                print(i)
                return

def main(argv):
    points = []
    fname = 'input10.txt'
    if len(argv) > 1:
        fname = argv[1]
    with open('input10.txt') as f:
        for line in f:
            x, y, vx, vy = map(int, re.findall('-?\d+', line))
            points.append(Point(x, y, vx, vy))
    solve(points)

if __name__ == '__main__':
    main(sys.argv)
