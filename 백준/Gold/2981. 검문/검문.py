from math import gcd
import sys

n = int(sys.stdin.readline())
number = list()
result = list()
minus = list()

for i in range(n):
    number.append(int(sys.stdin.readline()))

number.sort()

for i in range(n - 1):
    minus.append(number[i + 1] - number[i])

before = minus[0]

for i in range(1, len(minus)):
    before = gcd(before, minus[i])

for i in range(2, int(before ** 0.5) + 1):
    if not before % i:
        result.append(i)
        result.append(before // i)

result.append(before)

result = list(set(result))
result.sort()
print(*result)