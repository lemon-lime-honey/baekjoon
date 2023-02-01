sieve_bool = [False, False] + [True] * (999999)
for i in range(2, int(1000000 ** 0.5)):
    if sieve_bool[i]:
        for j in range(2 * i, 1000000, i):
            sieve_bool[j] = False

t = int(input())

for i in range(t):
    n = int(input())
    cnt = 0
    for j in range(2, n // 2 + 1):
        if sieve_bool[j] and sieve_bool[n - j]:
            cnt += 1
    print(cnt)