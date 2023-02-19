n = int(input())
result = 0

for i in range(n):
    ipt = input()
    stack = list()

    for index, letter in enumerate(ipt):
        if not stack:
            stack.append(letter)
        else:
            if stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)
    
    if not stack:
        result += 1

print(result)