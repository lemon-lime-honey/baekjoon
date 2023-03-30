ipt = input()
stack = list()
number = 1
result = 0

for i in range(len(ipt)):
    if ipt[i] == '(':
        number *= 2
        stack.append(ipt[i])
    elif ipt[i] == '[':
        number *= 3
        stack.append(ipt[i])
    elif ipt[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if ipt[i - 1] == '(':
            result += number
        number //= 2
        stack.pop()
    elif ipt[i] ==']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if ipt[i - 1] == '[':
            result += number
        number //= 3
        stack.pop()

print(0 if stack else result)