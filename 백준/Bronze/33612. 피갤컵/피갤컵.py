n = int(input())
result = [2024, 8]

result[1] += 7 * (n - 1)
result[0] += result[1] // 12
result[1] %= 12

if result[1] == 0:
    result[1] = 12
    result[0] -= 1

print(*result)
