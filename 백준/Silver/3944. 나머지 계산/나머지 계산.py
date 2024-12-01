import sys
input = sys.stdin.readline

t = int(input())
result = list()

for i in range(t):
    ipt = input().split()
    result.append(sum(map(int, list(ipt[1]))) % (int(ipt[0]) - 1))

print(*result, sep="\n")
