import sys

n = int(sys.stdin.readline())
cnt = 0

for i in range(n):
    temp = list(map(str, sys.stdin.readline().split('-')))
    if int(temp[1]) <= 90:
        cnt += 1

print(cnt)