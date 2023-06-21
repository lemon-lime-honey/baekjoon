a, b = map(int, input().split())
result = 0

sieve = [False, False] + [True] * (int(b ** 0.5) + 1)

for i in range(int(b ** .5) + 1):
    if sieve[i]:
        for j in range(2 * i, int(b ** .5) + 1, i):
            sieve[j] = False

for i in range(2, int(b ** 0.5) + 1):
    if i ** 2 > b: break
    if sieve[i]:
        ref = i ** 2
        while ref <= b:
            if ref >= a: result += 1
            ref *= i

print(result)