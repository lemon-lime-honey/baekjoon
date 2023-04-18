import sys
input = sys.stdin.readline


def prime(n):
    if n < 2: return 2
    while True:
        for number in range(2, int(n**0.5) + 1):
            if not n % number: break
        else: return n
        n += 1


t = int(input())

for i in range(t):
    n = int(input())
    print(prime(n))