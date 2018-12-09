import sys
from collections import Counter

def solve(elves, marbles):
    scores = Counter()
    ring = [0]
    elf = 0
    cursor = 0
    cur_marble = 1
    while cur_marble < marbles:
        if cur_marble % 23 == 0:
            scores[elf] += cur_marble
            cursor = (cursor - 7) % len(ring)
            scores[elf] += ring.pop(cursor)
        else:
            cursor = (cursor + 2) % len(ring)
            ring.insert(cursor, cur_marble)
        #print(f'[{elf+1}] {ring} ({ring[cursor]})')
        cur_marble += 1
        elf = (elf + 1) % elves
    return max(scores.values())

def main(argv):
    if len(argv) > 1:
        elves = int(argv[1])
        marbles = int(argv[2])
    else:
        with open('input09.txt') as f:
            parts = f.read().split()
        elves = int(parts[0])
        marbles = int(parts[6])
    print(solve(elves, marbles))

if __name__ == '__main__':
    main(sys.argv)
