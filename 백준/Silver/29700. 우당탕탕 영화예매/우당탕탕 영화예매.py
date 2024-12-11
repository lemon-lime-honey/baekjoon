import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
maps = [input().rstrip() for i in range(n)]
target = "0" * k
result = 0

for i in range(n):
    for j in range(m - k + 1):
        if maps[i][j] == "0":
            if maps[i][j: j + k] == target:
                result += 1

print(result)
