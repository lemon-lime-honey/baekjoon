import sys

n, m = map(int, sys.stdin.readline().split())
ref = list()
cnt = 0

for i in range(n):
    ref.append(sys.stdin.readline().strip())

for i in range(m):
    comp = sys.stdin.readline().strip()
    if comp in ref:
        cnt += 1

print(cnt)