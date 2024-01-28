from math import ceil

minimum, maximum = map(int, input().split())

n = int(maximum ** 0.5) + 1
prime = [True for i in range(n)]
prime[0] = False

for i in range(2, int(n ** 0.5) + 1):
    if prime[i]:
        for j in range(2 * i, n, i):
            prime[j] = False

sieve = [True for i in range(minimum, maximum + 1)]

for i in range(2, n):
    if prime[i]:
        chk = i * i
        ref = ceil(minimum / chk)
        chk *= ref

        while chk <= maximum:
            sieve[chk - minimum] = False
            chk = chk * (ref + 1) // ref
            ref += 1

result = 0

for flag in sieve:
    if flag: result += 1

print(result)