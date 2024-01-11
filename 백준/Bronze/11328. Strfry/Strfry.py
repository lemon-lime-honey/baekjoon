from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b = map(Counter, input().split())
    print('Possible' if a == b else 'Impossible')