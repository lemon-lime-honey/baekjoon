import sys
input = sys.stdin.readline


def find(a):
    if gates[a] != a:
        gates[a] = find(gates[a])
    return gates[a]


def union(a, b):
    a, b = find(a), find(b)
    if a == b: return
    if a > b: gates[a] = b
    else: gates[b] = a


g = int(input())
p = int(input())
gates = [i for i in range(g + 1)]
planes = [int(input()) for i in range(p)]
result = 0

for plane in planes:
    gate = find(plane)
    if gate == 0: break

    union(plane, gate - 1)
    result += 1

print(result)