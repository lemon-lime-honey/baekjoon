import sys
from math import gcd

input = sys.stdin.readline

q = int(input())

for i in range(q):
    a, b = map(int, input().split())
    if b % a == 0 and 2 * a <= b:
        print(1)
    else:
        print(0)
