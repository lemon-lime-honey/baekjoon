import sys

n = int(sys.stdin.readline())

if n == 1: print(0)
else:
    sieve_bool = [False, False] + [True] * (n - 1)
    sieve = list()

    for i in range(2, n + 1):
        if sieve_bool[i]:
            sieve.append(i)
            for j in range(2 * i, n + 1, i):
                sieve_bool[j] = False

    up = 0
    down = 0
    result = 0
    total = sieve[0]

    while up < len(sieve):
        if total < n:
            up += 1
            if up == len(sieve):
                break
            total += sieve[up]
        elif total == n:
            total -= sieve[down]
            result += 1
            down += 1
        elif total > n:
            total -= sieve[down]
            down += 1

    print(result)