n = int(input())

result = [int(1e12), 0, 0, 0]

for i in range(1, int(n**0.5) + 1):
    if n % i:
        continue
    for j in range(1, int(n**0.5) + 1):
        if n % j:
            continue
        k = n // i // j

        if i * j * k != n:
            continue

        chk = 2 * (i * j + j * k + k * i)

        if chk < result[0]:
            result[0] = chk
            result[1] = i
            result[2] = j
            result[3] = k

print(*result[1:])
