import sys
input = sys.stdin.readline

n = int(input())
scores = [int(input()) for i in range(n)]
result = 0

for i in range(n - 2, -1, -1):
    if scores[i] < scores[i + 1]: continue
    result += scores[i] - scores[i + 1] + 1
    scores[i] = scores[i + 1] - 1

print(result)