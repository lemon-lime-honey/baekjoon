import sys
input = sys.stdin.readline

n = int(input())
space = list(map(int, input().split()))
reach, cnt, last = 0, 0, 0

for i in range(len(space) - 1):
    reach = max(reach, i + space[i])
    if i == last:
        last = reach
        cnt += 1

print(cnt if n - 1 <= last else -1)
