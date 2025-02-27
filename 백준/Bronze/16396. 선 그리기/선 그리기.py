n = int(input())
line = [False for i in range(10001)]
result = 0

for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, y):
        line[j] = True

for i in range(1, 10001):
    if line[i]:
        result += 1

print(result)
