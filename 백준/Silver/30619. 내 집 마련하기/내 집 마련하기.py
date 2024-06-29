import sys
input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))
m = int(input())
result = list()

data = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    data[a[i]] = i

for i in range(m):
    l, r = map(int, input().split())
    res = data[:l] + sorted(data[l: r+1]) + data[r+1:]
    result.append([0 for j in range(n + 1)])
    for j in range(1, n + 1):
        result[-1][res[j]] = j

for res in result:
    print(*res[1:])
