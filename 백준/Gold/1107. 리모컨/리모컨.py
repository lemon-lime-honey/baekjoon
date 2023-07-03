import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = set()

if m: broken = set(input().rstrip().split())

result = abs(100 - n)

for i in range(1000001):
    for num in str(i):
        if num in broken:
            break
    else:
        result = min(result, len(str(i)) + abs(i - n))

print(result)