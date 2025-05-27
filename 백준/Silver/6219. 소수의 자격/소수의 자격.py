prime = [True for i in range(4000001)]
prime[0] = False
prime[1] = False

for i in range(2, 2 * 10 ** 3 + 1):
    if prime[i]:
        for j in range(2 * i, 4000001, i):
            prime[j] = False

a, b, d = map(int, input().split())
result = 0

for num in range(a, b + 1):
    if prime[num] and str(d) in str(num):
        result += 1

print(result)
