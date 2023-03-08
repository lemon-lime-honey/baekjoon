import sys

def exp(n, m):
    if m == 1: return n % 1000000007
    res = exp(n, m // 2)
    return (res * res * n) % 1000000007 if m % 2 else (res * res) % 1000000007

a = int(sys.stdin.readline())
x = int(sys.stdin.readline())
result = exp(a, x)
print(result)