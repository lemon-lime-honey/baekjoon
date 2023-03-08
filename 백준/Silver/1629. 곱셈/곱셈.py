import sys

def exp(a, b, c):
    if b == 1: return a % c
    res = exp(a, b // 2, c)
    return (res * res * a) % c if b % 2 else (res * res) % c

a, b, c = map(int, sys.stdin.readline().split())
result = exp(a, b, c)
print(result)