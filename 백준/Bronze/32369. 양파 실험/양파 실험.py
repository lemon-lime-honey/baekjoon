n, a, b = map(int, input().split())
result = [1, 1]

for i in range(n):
    result[0] += a
    result[1] += b
    if result[0] < result[1]:
        result[0], result[1] = result[1], result[0]
    elif result[0] == result[1]:
        result[1] -= 1

print(*result)
