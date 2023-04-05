from math import gcd
import sys
input = sys.stdin.readline

n = int(input())
space = list()
before = int(input())

for i in range(n - 1):
    tree = int(input())
    space.append(tree - before)
    before = tree

number = gcd(*space)
total = 1

for i in range(n - 1):
    total += space[i] // number

print(total - n)