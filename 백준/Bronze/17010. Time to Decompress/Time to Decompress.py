import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    ipt = input().split()
    print(ipt[1] * int(ipt[0]))
