import sys
input = sys.stdin.readline

n = int(input())
result = list()

for i in range(n):
    a, b, x = map(int, input().split())
    result.append(a * (x - 1) + b)

print(*result, sep='\n')
