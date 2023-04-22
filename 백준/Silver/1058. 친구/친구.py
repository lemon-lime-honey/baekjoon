import sys
input = sys.stdin.readline

n = int(input())
relations = [[int(1e9) for i in range(n)] for j in range(n)]
result = [0 for i in range(n)]

for i in range(n):
    temp = input().strip()
    for j in range(n):
        if i == j:
            relations[i][j] = 0
        elif temp[j] == 'Y':
            relations[i][j] = 1

for i in range(n):
    for j in range(n):
        for k in range(n):
            if relations[j][i] + relations[i][k] < relations[j][k]:
                relations[j][k] = relations[j][i] + relations[i][k]

for i in range(n):
    people = 0
    for j in range(n):
        if relations[i][j] in (1, 2):
            people += 1
    result[i] = people

print(max(result))