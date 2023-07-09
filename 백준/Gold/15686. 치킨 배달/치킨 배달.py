from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
household = list()
chicken = list()
cities = list()
result = int(1e9)

for i in range(n):
    cities.append(list(map(int, input().split())))
    for j in range(n):
        if cities[i][j] == 1:
            household.append((i, j))
        elif cities[i][j] == 2:
            chicken.append((i, j))

chicken_comb = combinations(chicken, m)

for chicken_set in chicken_comb:
    house = [int(1e9) for i in range(len(household))]
    for r, c in chicken_set:
        for i in range(len(house)):
            house[i] = min(house[i], abs(household[i][0] - r) + abs(household[i][1] - c))
    result = min(result, sum(house))

print(result)