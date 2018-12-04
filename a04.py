from collections import defaultdict, Counter

with open('input04.txt') as f:
    lines = [l.strip() for l in f]

lines.sort()
guards = defaultdict(list)
for line in lines:
    if 'begins' in line:
        gid = int(line.split()[3].lstrip('#'))
    elif 'falls' in line:
        begin = int(line[15:17])
    elif 'wakes' in line:
        end = int(line[15:17])
        guards[gid].append(range(begin, end))

max_guard, ranges = max(guards.items(), key=lambda i: sum(len(r) for r in i[1]))
minutes = Counter()
for minute in range(0, 60):
    for r in ranges:
        if minute in r:
            minutes[minute] += 1

print(minutes.most_common(1)[0][0] * max_guard)

cnt = Counter()
for guard, ranges in guards.items():
    for r in ranges:
        for minute in range(0, 60):
            if minute in r:
                cnt[guard, minute] += 1
max_guard, max_minute = cnt.most_common(1)[0][0]
print(max_guard*max_minute)
