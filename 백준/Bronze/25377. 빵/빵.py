import sys

n = int(sys.stdin.readline())
result = list()

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a <= b:
        result.append(b)

try:
    print(min(result))
except:
    print(-1)