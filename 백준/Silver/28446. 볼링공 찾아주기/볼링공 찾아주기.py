import sys

input = sys.stdin.readline

m = int(input())
ball = dict()
result = list()

for i in range(m):
    ipt = list(map(int, input().split()))
    if ipt[0] == 1:
        ball[ipt[2]] = ipt[1]
    else:
        result.append(ball[ipt[1]])

print(*result, sep="\n")
