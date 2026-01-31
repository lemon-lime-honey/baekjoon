a, b = map(int, input().split())
n = int(input())
freq = [int(input()) for i in range(n)]

result = abs(b - a)

for f in freq:
    target = abs(b - f) + 1
    result = min(result, target)

print(result)
