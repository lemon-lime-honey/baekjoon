a, b, n, w = map(int, input().split())

result = [0, 0, 0]

for i in range(1, n):
    x, y = i, n - i
    if x * a + y * b == w:
        result[0] = x
        result[1] = y
        result[2] += 1

if result[2] != 1:
    print(-1)
else:
    print(result[0], result[1])
