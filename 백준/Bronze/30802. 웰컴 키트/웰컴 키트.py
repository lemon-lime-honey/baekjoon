from math import ceil
import sys
input = sys.stdin.readline

n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

print(sum([ceil(size[i] / t) for i in range(6)]))
print(n // p, n % p)