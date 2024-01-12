import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
people = [[int(1e9) for i in range(n + 1)] for j in range(n + 1)]
result = 0

for i in range(m):
    a, b = map(int, input().split())
    people[a][b] = 1
    people[b][a] = 1

for i in range(1, n + 1):
    people[i][i] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if people[j][i] + people[i][k] < people[j][k]:
                people[j][k] = people[j][i] + people[i][k]

for i in range(2, n + 1):
    if people[1][i] < 3:
        result += 1

print(result)