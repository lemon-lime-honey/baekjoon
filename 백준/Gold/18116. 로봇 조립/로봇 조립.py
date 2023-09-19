import sys
input = sys.stdin.readline


def find(p):
    if parts[p] != p:
        parts[p] = find(parts[p])
    return parts[p]


def union(p, q):
    p, q = find(p), find(q)
    if p == q: return
    parts[max(p, q)] = min(p, q)
    robot[min(p, q)] += robot[max(p, q)]


n = int(input())
parts = [i for i in range(10 ** 6 + 1)]
robot = [1 for i in range(10 ** 6 + 1)]

for i in range(n):
    ipt = input().rstrip().split()

    if len(ipt) == 2:
        print(robot[find(int(ipt[-1]))])
    else:
        p, q = int(ipt[1]), int(ipt[2])
        union(p, q)