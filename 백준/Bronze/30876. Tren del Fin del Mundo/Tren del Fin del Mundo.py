n = int(input())
result = [0, int(1e9)]

for i in range(n):
    x, y = map(int, input().split())
    if y < result[1]:
        result[0] = x
        result[1] = y

print(*result)
