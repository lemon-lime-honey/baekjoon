s = input()

stack = list()
result = 0

for e in s:
    if e == "(":
        stack.append(e)
    elif not stack:
        result += 1
    else:
        stack.pop()

print(result + len(stack))
