import sys
from itertools import product

def power(x, y, serial):
    rid = x + 10
    p = rid
    p *= y
    p += serial
    p *= rid
    p = int(f'{p:03}'[-3])
    p -= 5
    return p

assert power(3, 5, 8) == 4
assert power(122, 79, 57) == -5
assert power(217, 196, 39) == 0
assert power(101, 153, 71) == 4

def solve(serial):
    grid = {}
    power3 = {}
    for x, y in product(range(1, 301), range(1, 301)):
        grid[x, y] = power(x, y, serial)

    for x, y in product(range(1, 301-3), range(1, 301 - 3)):
        p3 = 0
        for i, j in product(range(3), range(3)):
            p3 += grid[x + i, y + j]
        power3[x, y] = p3
    print(','.join(str(a) for a in max(power3, key=lambda c: power3[c])))

if __name__ == '__main__':
    solve(int(sys.argv[1]))
