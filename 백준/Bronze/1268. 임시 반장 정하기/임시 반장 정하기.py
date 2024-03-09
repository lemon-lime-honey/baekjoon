from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
result = [0 for i in range(n)]
record = [list(map(int, input().split())) for i in range(n)]
combs = combinations(range(n), 2)

for comb in combs:
    for i in range(5):
        if record[comb[0]][i] == record[comb[1]][i]:
            result[comb[0]] += 1
            result[comb[1]] += 1
            break

print(result.index(max(result)) + 1)