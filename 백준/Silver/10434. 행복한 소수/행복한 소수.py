import sys

input = sys.stdin.readline


def calc(n):
    num = n
    seen = {n}

    while num != 1:
        temp = 0
        while num:
            temp += (num % 10) ** 2
            num //= 10
        num = temp
        if num in seen:
            break
        seen.add(num)

    return num == 1


sieve = [True for i in range(10001)]
sieve[0], sieve[1] = False, False

for i in range(101):
    if sieve[i]:
        for j in range(2 * i, 10001, i):
            sieve[j] = False

p = int(input())

for i in range(p):
    t, m = map(int, input().split())
    if sieve[m] and calc(m):
        print(f"{t} {m} YES")
    else:
        print(f"{t} {m} NO")
