import sys
input = sys.stdin.readline

n = int(input())
stack = list()
result = 0

for i in range(n):
    ipt = list(map(int, input().split()))
    if ipt[0] == 0 and stack:
        stack[-1][1] -= 1
        if stack[-1][1] == 0:
            result += stack.pop()[0]
    elif ipt[0] == 1:
        if ipt[2] == 1:
            result += ipt[1]
        else:
            stack.append([ipt[1], ipt[2] - 1])

print(result)