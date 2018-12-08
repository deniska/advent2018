import sys
import networkx as nx
from collections import deque

def solve(puzzle):
    g = nx.DiGraph()
    for n1, n2 in puzzle:
        g.add_edge(n1, n2)
    return ''.join(nx.algorithms.dag.lexicographical_topological_sort(g))

def solve2(puzzle):
    max_workers = 5
    baseline = 60
    g = nx.DiGraph()
    for n1, n2 in puzzle:
        g.add_edge(n1, n2)
    workers = {}
    seconds = 0
    queue = deque()
    queue.append(solve(puzzle)[0])
    while True:
        for worker in workers:
            workers[worker] -= 1
        for k, v in list(workers.items()):
            if v == 0:
                workers.pop(k)
                g.remove_node(k)
        for n in g:
            if n in workers:
                continue
            if not list(g.predecessors(n)) and not n in queue:
                queue.append(n)
        while len(workers) < max_workers and queue:
            n = queue.popleft()
            workers[n] = baseline + ord(n) - ord('A') + 1
        if not queue and not workers:
            break
        seconds += 1
    return seconds

def main(argv):
    fname = 'input07.txt'
    if len(argv) > 1:
        fname = argv[1]
    puzzle = []
    with open(fname) as f:
        for line in f:
            parts = line.split()
            puzzle.append((parts[1], parts[7]))
    print(solve(puzzle))
    print(solve2(puzzle))

if __name__ == '__main__':
    main(sys.argv)
