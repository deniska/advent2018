import itertools
freq = 0
nums = []
with open('input01.txt') as f:
    for line in f:
        num = int(line)
        nums.append(num)
        freq += num
print(freq)

freq = 0
seen = set([0])
for num in itertools.cycle(nums):
    freq += num
    if freq in seen:
        print(freq)
        break
    seen.add(freq)
