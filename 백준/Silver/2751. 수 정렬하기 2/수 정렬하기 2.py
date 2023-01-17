import sys

n = int(input())
num = list()

for i in range(n):
    num.append(int(sys.stdin.readline()))

print(*sorted(num), sep = '\n')
