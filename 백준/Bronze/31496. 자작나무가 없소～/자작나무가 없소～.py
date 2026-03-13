import sys

input = sys.stdin.readline

ipt = input().split()

n = int(ipt[0])
target = ipt[1]
result = 0

for i in range(n):
    ipt = input().split()
    targets = ipt[0].split("_")
    for t in targets:
        if t == target:
            result += int(ipt[1])
            break

print(result)
