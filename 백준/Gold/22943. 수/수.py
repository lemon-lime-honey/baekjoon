from itertools import permutations


def get_numbers(idx, route):
    for numset in permutations(range(10), k):
        if numset[0] == 0: continue
        nums.append(int(''.join(map(str, numset))))


def chk_sum(num):
    for i in range(2, num):
        if i != num - i and sieve[i] and sieve[num - i]:
            return True

    return False


def chk_cross(num):
    while num:
        if num % m: break
        num //= m

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and sieve[i] and sieve[num // i]:
            return True

    return False


sieve = [True for i in range(10**6)]
sieve[0], sieve[1] = False, False

for i in range(2, 10**3 + 1):
    if sieve[i]:
        for j in range(2 * i, 10 ** 6, i):
            sieve[j] = 0


k, m = map(int, input().split())
chk = [False for i in range(10)]
nums = list()
result = 0

get_numbers(0, '')

for num in nums:
    if chk_cross(num) and chk_sum(num):
        result += 1

print(result)