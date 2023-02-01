import sys

sieve_bool = [False, False] + [True] * (1000000 - 1)
for i in range(2, int(1000000 ** 0.5)):
    if sieve_bool[i]:
        for j in range(2 * i, 1000001, i):
            sieve_bool[j] = False

while True:
    n = int(sys.stdin.readline())
    if not n:
        break
    for i in range(3, 1000000):
        if sieve_bool[i] * sieve_bool[n - i]:
            print(f'{n} = {i} + {n - i}')
            break
    else:
        print("Goldbach's conjecture is wrong.")