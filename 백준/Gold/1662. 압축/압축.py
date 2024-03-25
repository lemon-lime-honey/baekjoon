import sys
input = sys.stdin.readline

compressed = input().rstrip()
n = len(compressed)
stack = list()

for i in range(n):
    if compressed[i] == ')':
        temp = 0
        while stack[-1] != '(':
            temp += stack.pop()
        stack.pop()
        stack.append(stack.pop() * temp)
    elif i < n - 1 and compressed[i].isdigit() and compressed[i + 1] == '(':
        stack.append(int(compressed[i]))
    elif compressed[i].isdigit():
        stack.append(1)
    else:
        stack.append(compressed[i])

print(sum(stack))