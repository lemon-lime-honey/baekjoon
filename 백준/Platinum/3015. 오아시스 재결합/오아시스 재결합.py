import sys
input = sys.stdin.readline

n = int(input())
stack = list()
result = 0

for i in range(n):
    now = int(input())
    cnt = 1

    while stack and stack[-1][0] < now:
        result += stack[-1][1]
        stack.pop()

    if stack:
        if stack[-1][0] == now:
            result += stack[-1][1]
            cnt = stack[-1][1] + 1
            stack.pop()
            if stack: result += 1
        else:
            result += 1

    stack.append((now, cnt))

print(result)