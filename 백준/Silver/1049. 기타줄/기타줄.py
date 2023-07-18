from math import ceil
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
six = list()
one = list()

for i in range(m):
    a, b = map(int, input().split())
    six.append(a)
    one.append(b)

six.sort()
one.sort()

print(min((n % 6) * one[0] + (n // 6) * six[0], ceil(n / 6) * six[0], n * one[0]))