import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))


def find(p):
    if nodes[p] != p:
        nodes[p] = find(nodes[p])
    return nodes[p]


def union(p, q):
    np, nq = find(p), find(q)

    if np != nq: nodes[nq] = np
    else:
        cycle.add(p)
        cycle.add(q)


case_num = 1

while True:
    n, m = map(int, input().split())
    if n == m == 0: break
    
    nodes = [i for i in range(n + 1)]
    cycle = set()
    
    for i in range(m):
        a, b = map(int, input().split())
        union(a, b)

    parent = set([find(node) for node in nodes[1:]])
    children = set([find(node) for node in cycle])
    cnt = len(parent.difference(children))

    if cnt == 0:
        print(f'Case {case_num}: No trees.')
    elif cnt == 1:
        print(f'Case {case_num}: There is one tree.')
    else:
        print(f'Case {case_num}: A forest of {cnt} trees.')

    case_num += 1