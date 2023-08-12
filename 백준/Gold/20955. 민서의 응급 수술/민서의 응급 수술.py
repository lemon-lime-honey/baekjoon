import sys
input = sys.stdin.readline


def find(a):
    if a != neuron[a]:
        neuron[a] = find(neuron[a])
    return neuron[a]


def union(a, b):
    a, b = find(a), find(b)
    if a == b: return True
    if a < b: neuron[b] = a
    else: neuron[a] = b
    return False


n, m = map(int, input().split())
neuron = [i for i in range(n + 1)]
result = 0

for i in range(m):
    u, v = map(int, input().split())
    if find(u) == find(v): result += 1
    union(u, v)

for i in range(1, n):
    chk = union(i, i + 1)
    if not chk: result += 1

print(result)