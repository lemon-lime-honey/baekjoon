ipt = input()
stack = list()
result = list()

for i in range(len(ipt)):
    if ipt[i].isalpha():
        result.append(ipt[i])
    elif ipt[i] == '(':
        stack.append(ipt[i])
    elif ipt[i] == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()
    elif ipt[i] in '*/':
        while stack and (stack[-1] in '*/'):
            result.append(stack.pop())
        stack.append(ipt[i])
    elif ipt[i] in '+-':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.append(ipt[i])

while stack:
    result.append(stack.pop())

print(''.join(result))