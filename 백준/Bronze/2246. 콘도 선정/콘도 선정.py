import sys

input = sys.stdin.readline

n = int(input())
data = [tuple(map(int, input().split())) for i in range(n)]

data.sort()
ref, result = 10001, 0

for distance, cost in data:
    if cost < ref:
        ref = cost
        result += 1
        
print(result)