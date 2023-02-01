n, k = map(int, input().split())
cnt = 0

sieve_bool = [False, False] + [True] * (n - 1)
for i in range(2, n + 1):
    if sieve_bool[i]:
        for j in range(i, n + 1, i):
            if sieve_bool[j]:
                sieve_bool[j] = False
                cnt += 1
                if cnt == k:
                    print(j)
                    break