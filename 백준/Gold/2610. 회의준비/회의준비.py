import sys
input = sys.stdin.readline


def find(p):
    if p != group[p]:
        group[p] = find(group[p])
    return group[p]


def union(p, q):
    p, q = find(p), find(q)
    if p < q:
        group[q] = p
    else:
        group[p] = q


n = int(input())
m = int(input())
data = [[int(1e9) for i in range(n + 1)] for j in range(n + 1)]
group = [i for i in range(n + 1)]
relations = list()

for i in range(1, n + 1):
    data[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    data[a][b] = 1
    data[b][a] = 1
    union(a, b)

for i in range(1, n + 1):
    find(i)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if data[j][k] <= data[j][i] + data[i][k]:
                continue
            data[j][k] = data[j][i] + data[i][k]

mems = dict()

for i in range(1, n + 1):
    target = find(i)
    if target not in mems:
        mems[target] = [i]
    else:
        mems[target].append(i)

print(len(mems))
result = list()

for member in mems.values():
    time = {x: 0 for x in member}
    for i in range(len(member)):
        for j in range(i + 1, len(member)):
            time[member[i]] = max(time[member[i]], data[member[i]][member[j]])
            time[member[j]] = max(time[member[j]], data[member[j]][member[i]])
    result.append(sorted(time.items(), key=lambda x: (x[1], x[0]))[0][0])

print(*sorted(result), sep='\n')