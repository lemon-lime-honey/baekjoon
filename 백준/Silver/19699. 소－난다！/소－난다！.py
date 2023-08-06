from itertools import combinations


def isPrime(number):
    ref = 2
    while ref * ref <= number:
        if not number % ref: return False
        ref += 1
    return True


n, m = map(int, input().split())
weights = list(map(int, input().split()))
cow_comb = list(combinations(weights, m))
result = set()

for cows in cow_comb:
    temp = 0
    for cow in cows:
        temp += cow
    if isPrime(temp): result.add(temp)

answer = sorted(list(result))

if not answer: print(-1)
else: print(*answer)