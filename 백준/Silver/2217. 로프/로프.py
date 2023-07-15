import sys
input = sys.stdin.readline

n = int(input())
weights = sorted([int(input()) for i in range(n)])
result = weights[-1]

for i in range(1, n + 1):
    if i * weights[n - i] >= result:
        result = i * weights[n - i]

print(result)