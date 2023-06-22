import sys
input = sys.stdin.readline

n = int(input())
stack = list()
result = 0

for i in range(n):
    x, y = map(int, input().split())
    while stack and stack[-1] > y:
        stack.pop()
        result += 1
    if stack and stack[-1] == y: continue
    stack.append(y)

while stack:
    chk = stack.pop()
    if chk: result += 1

print(result)