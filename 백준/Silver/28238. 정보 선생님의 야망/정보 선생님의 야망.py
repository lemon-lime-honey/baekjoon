from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input())
schedule = [list(map(int, input().split())) for i in range(n)]
result = [-1, [0 for i in range(5)]]
combs = combinations(range(5), 2)

for first, second in combs:
    cnt = 0

    for s in schedule:
        if s[first] == s[second] == 1:
            cnt += 1

    if result[0] < cnt:
        result[0] = cnt
        result[1] = [0, 0, 0, 0, 0]
        result[1][first] = 1
        result[1][second] = 1

print(result[0])
print(*result[1])
