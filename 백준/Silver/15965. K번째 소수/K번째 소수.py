sieve_bool = [False, False] + [True] * 499999

for i in range(2, int(500000 ** 0.5)):
    if sieve_bool[i]:
        for j in range(2 * i, 500001, i):
            sieve_bool[j] = False

k = int(input())
cnt = 0

for i in range(500001):
    if sieve_bool[i]:
        cnt += 1
        if cnt == k:
            print(i)
            break