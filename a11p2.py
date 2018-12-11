import sys
from itertools import product
import numpy as np
from a11 import power

LOW = -7

def solve(serial):
    grid = np.ndarray((301, 301), dtype=np.int32)
    for x, y in product(range(301), range(301)):
        grid[x, y] = power(x, y, serial)
    max_coord = 0, 0, 0
    max_val = LOW
    for size in range(1, 300):
        for x, y in product(range(1, 301-size), range(1, 301-size)):
            s = np.sum(grid[x:x+size, y:y+size])
            if s > max_val:
                max_val = s
                max_coord = x, y, size
        x, y, s = max_coord
        print(f'{x},{y},{s}')

if __name__ == '__main__':
    solve(int(sys.argv[1]))
