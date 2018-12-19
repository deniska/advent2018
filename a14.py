import sys
import collections

def solve(num):
    recipes = [3, 7]
    e0 = 0
    e1 = 1
    while len(recipes) < num + 10:
        d = recipes[e0] + recipes[e1]
        if d >= 10:
            recipes.extend([1, d-10])
        else:
            recipes.append(d)
        e0 += 1 + recipes[e0]
        e0 %= len(recipes)
        e1 += 1 + recipes[e1]
        e1 %= len(recipes)
    print(''.join(str(x) for x in recipes[num:num+10]))

def solve2(num):
    dnum = collections.deque(num)
    last = collections.deque(maxlen=len(num))
    recipes = [3, 7]
    e0 = 0
    e1 = 1
    while True:
        d = recipes[e0] + recipes[e1]
        if d >= 10:
            recipes.append(1)
            last.append(1)
            if last == dnum:
                break
            recipes.append(d-10)
            last.append(d-10)
        else:
            recipes.append(d)
            last.append(d)
        e0 += 1 + recipes[e0]
        e0 %= len(recipes)
        e1 += 1 + recipes[e1]
        e1 %= len(recipes)
        if last == dnum:
            break
    print(len(recipes) - len(num))

if __name__ == '__main__':
    solve(int(sys.argv[1]))
    solve2(list(map(int, sys.argv[1])))
