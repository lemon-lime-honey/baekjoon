n = int(input())
result = 0
k = 1

while n:
    result += 1
    if 1 <= n < k:
        n -= 1
        k = 2
    else:
        n -= k
        k += 1

print(result)