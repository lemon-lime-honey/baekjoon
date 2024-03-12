import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
sleepy = list(map(int, input().split()))
targets = list(map(int, input().split()))
area = [list(map(int, input().split())) for i in range(m)]
record = [0 for i in range(n + 3)]

for s in sleepy:
    record[s] -= 1

for t in targets:
    if record[t] == -1: continue
    for i in range(t, n + 3, t):
        if record[i] != -1:
            record[i] = 1

prefix = [0 for i in range(n + 3)]

for i in range(3, n + 3):
    prefix[i] = prefix[i - 1]
    if record[i] != 1:
        prefix[i] += 1

result = list()

for s, e in area:
    result.append(prefix[e] - prefix[s - 1])

print(*result, sep='\n')