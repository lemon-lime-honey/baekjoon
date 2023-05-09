import sys
input = sys.stdin.readline


def find(p):
    if p != people[p]:
        people[p] = find(people[p])
    return people[p]


def union(p, q):
    p, q = find(p), find(q)
    if p == q: return
    if p > q: people[p] = q
    else: people[q] = p


t = int(input())

for i in range(t):
    n = int(input())
    k = int(input())

    people = [j for j in range(n)]

    for j in  range(k):
        a, b = map(int, input().split())
        union(a, b)
    
    m = int(input())
    print(f'Scenario {i + 1}:')

    for j in range(m):
        u, v = map(int, input().split())
        print(1 if find(u) == find(v) else 0)
    
    print()