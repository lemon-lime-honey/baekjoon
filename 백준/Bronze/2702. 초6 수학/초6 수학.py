import sys

input = sys.stdin.readline


def get_gcd(n, m):
    if n % m:
        return get_gcd(m, n % m)
    return m


t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    gcd = get_gcd(max(a, b), min(a, b))
    print(a * b // gcd, gcd)
