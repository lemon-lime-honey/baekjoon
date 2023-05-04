import sys
input = sys.stdin.readline


def find(n):
    if n != bridge[n]:
        bridge[n] = find(bridge[n])
    return bridge[n]


def union(n1, n2):
    n1, n2 = find(n1), find(n2)

    if n1 == n2: return
    if n1 > n2: bridge[n1] = n2
    else: bridge[n2] = n1


n = int(input())
bridge = [i for i in range(n + 1)]

for i in range(n - 2):
    a, b = map(int, input().split())
    union(a, b)

target = set()

for i in range(1, n + 1):
    temp = find(i)
    if temp not in target:
        target.add(temp)

print(*target)