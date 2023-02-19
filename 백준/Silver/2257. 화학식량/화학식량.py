size = {'H': 1, 'C': 12, 'O': 16}

ipt = input()
stack = list()

for element in ipt:
    if element == '(':
        stack.append(element)
    elif element == ')':
        temp = 0
        while True:
            now = stack.pop()
            if now == '(':
                stack.append(temp)
                break
            else:
                temp += now
    elif element.isdigit():
        temp = stack.pop()
        stack.append(temp * int(element))
    else:
        stack.append(size[element])

print(sum(stack))