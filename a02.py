from collections import Counter
import itertools

count2 = 0
count3 = 0
ids = []
with open('input02.txt') as f:
    for line in f:
        line = line.strip()
        ids.append(line)
        c = Counter(line)
        if 2 in c.values():
            count2 += 1
        if 3 in c.values():
            count3 += 1

print(count2 * count3)

for id1, id2 in itertools.product(ids, ids):
    if id1 == id2:
        continue
    diff = 0
    diffpos = 0
    for pos, (c1, c2) in enumerate(zip(id1, id2)):
        if c1 != c2:
            diff += 1
            diffpos = pos
        if diff > 1:
            break
    if diff == 1:
        print(id1)
        print(id2)
        print(id1[:diffpos] + id1[diffpos+1:])
        break
