sieve = [True for i in range(10**6 + 1)]
sieve[0], sieve[1] = False, False

for i in range(2, int(10**3 + 1)):
    if sieve[i]:
        for j in range(2 * i, 10**6 + 1, i):
            sieve[j] = False

n = int(input())
a = set(map(int, input().split()))
result = 1

for num in a:
    if sieve[num]: result *= num

print(-1 if result == 1 else result)