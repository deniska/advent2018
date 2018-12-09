import sys
from collections import Counter, deque

def solve(elves, marbles):
    scores = Counter()
    ring = deque([0])
    elve = 0
    cur_marble = 1
    while cur_marble < marbles:
        if cur_marble % 23 == 0:
            scores[elve] += cur_marble
            ring.rotate(7)
            scores[elve] += ring.popleft()
        else:
            ring.rotate(-2)
            ring.appendleft(cur_marble)
        #print(f'[{elve+1}] {ring} ({ring[cursor]})')
        cur_marble += 1
        elve = (elve + 1) % elves
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
