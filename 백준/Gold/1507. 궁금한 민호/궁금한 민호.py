from copy import deepcopy
import sys
input = sys.stdin.readline

n = int(input())
cities = [list(map(int, input().split())) for i in range(n)]
original = deepcopy(cities)
result = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or i == k: continue
            if cities[j][k] == cities[j][i] + cities[i][k]:
                original[j][k] = 0
            elif cities[j][k] > cities[j][i] + cities[i][k]:
                print(-1)
                sys.exit()

for i in range(n):
    for j in range(n):
        result += original[i][j]

print(result // 2)