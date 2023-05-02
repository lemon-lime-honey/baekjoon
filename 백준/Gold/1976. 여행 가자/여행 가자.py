import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))


def find(num):
    if num != cities[num]:
        cities[num] = find(cities[num])
    return cities[num]


def union(n1, n2):
    n1, n2 = find(n1), find(n2)

    if n1 == n2: return
    if n1 < n2: cities[n2] = n1
    else: cities[n1] = n2


n = int(input())
m = int(input())
cities = [i for i in range(n + 1)]

for i in range(1, n + 1):
    ipt = list(map(int, input().split()))
    for j in range(n):
        if ipt[j] == 1:
            union(i, j + 1)

travel = list(map(int, input().split()))
root = find(travel[0])

for city in travel:
    if find(city) != root:
        print('NO')
        break
else: print('YES')