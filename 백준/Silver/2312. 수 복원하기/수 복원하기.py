sieve_bool = [False, False] + [True] * (999999)
for i in range(2, int(1000000 ** 0.5)):
    if sieve_bool[i]:
        for j in range(2 * i, 1000000, i):
            sieve_bool[j] = False

t = int(input())

for i in range(t):
    n = int(input())
    for j in range(n + 1):
        if sieve_bool[j] and (n % j == 0):
            cnt = 0
            temp = n
            while True:
                cnt += 1
                temp //= j
                if temp % j:
                    break
            print(f'{j} {cnt}')