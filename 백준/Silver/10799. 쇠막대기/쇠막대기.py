stick = input()
stack = list()
result = 0

for index, element in enumerate(stick):
    if element == '(':
        stack.append(element)
    else:
        stack.pop()
        if stick[index - 1] == '(':
            result += len(stack)
        else:
            result += 1

print(result)