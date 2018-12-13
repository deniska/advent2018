import sys

def neighbors(idx, state):
    return tuple(x in state for x in range(idx-2, idx+3))

def solve(initial, states, gens=20):
    state = {x for x, c in enumerate(initial) if c == '#'}
    plant_states = set()
    for s, p in states.items():
        if p != '#':
            continue
        plant_states.add(tuple(c == '#' for c in s))
    for g in range(gens):
        next_state = set()
        for i in range(min(state)-5, max(state)+5):
            if neighbors(i, state) in plant_states:
                next_state.add(i)
        state = next_state
    return sum(state)

def main(argv):
    states = {}
    fname = 'input12.txt'
    if len(argv) > 1:
        fname = argv[1]
    with open(fname) as f:
        initial = next(f).strip().split()[2]
        next(f) # skip
        for line in f:
            a, b = line.strip().split(' => ')
            states[a] = b
    print(solve(initial, states))
    c2000 = solve(initial, states, 2000) # it's linear after a certain point \o/
    c3000 = solve(initial, states, 3000)
    print(c2000 + (c3000-c2000) * ((50000000000-2000)//1000))

if __name__ == '__main__':
    main(sys.argv)
