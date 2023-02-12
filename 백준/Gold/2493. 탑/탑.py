import sys
n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
result = [0] * n
stack = list()

for i in range(n):
    while stack:
        if stack[-1][0] > tower[i]:
            result[i] = stack[-1][1] + 1
            break
        else:
            stack.pop()
    stack.append((tower[i], i))

print(*result)