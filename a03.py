import collections
import sys
import re
claims = []
claimed = collections.Counter()

fname = 'input03.txt'
if len(sys.argv) > 1:
    fname = sys.argv[1]
with open(fname) as f:
    for line in f:
        m = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
        claims.append((int(m[1]), int(m[2]), int(m[3]),
                        int(m[4]), int(m[5])))

for id, x, y, w, h in claims:
    for xx in range(x, x+w):
        for yy in range(y, y+h):
            claimed[xx, yy] += 1
claimed_cnt = 0
for v in claimed.values():
    if v > 1:
        claimed_cnt += 1
print(claimed_cnt)

def is_non_overlapping(x, y, w, h):
    for xx in range(x, x+w):
        for yy in range(y, y+h):
            if claimed[xx, yy] != 1:
                return False
    return True

for id, x, y, w, h in claims:
    if is_non_overlapping(x, y, w, h):
        print(id)
        break
