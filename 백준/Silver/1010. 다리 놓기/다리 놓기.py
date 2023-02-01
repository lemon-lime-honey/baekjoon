from math import comb

t = int(input())

for i in range(t):
    num = list(map(int, input().split()))
    num.sort()
    print(comb(num[1], num[0]))