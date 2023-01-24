import sys

sieve = [False, False] + [True for x in range(10000)]

for i in range(2, int((10001) ** 0.5)):
    if sieve[i] == True:
        for j in range(2 * i, 10001, i):
            sieve[j] = False

t = int(sys.stdin.readline())

for i in range(t):
    num = int(sys.stdin.readline())
    target = list()
    j = 2

    while j <= num:
        if sieve[j] * sieve[num - j] * (j <= (num - j)):
            target.append(j)
        j += 1
    
    print(max(target), num - max(target))