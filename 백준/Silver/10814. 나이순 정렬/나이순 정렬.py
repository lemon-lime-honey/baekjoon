import sys

n = int(input())
memberInfo = list()

for i in range(n):
    memberInfo.append(list(sys.stdin.readline().split()))

memberInfo.sort(key = lambda x: int(x[0]))

for i in range(n):
    print(*memberInfo[i])
