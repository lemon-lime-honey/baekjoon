from functools import reduce
from math import gcd

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

num1 = reduce(lambda i, j: i * j, a)
num2 = reduce(lambda i, j: i * j, b)

print(f"{gcd(num1, num2)}"[-9:])
