n = int(input())
number = list(map(int, input().split()))
stack = list()
result = [-1] * n

for index, num in enumerate(number):
    while stack:
        if stack[-1][0] < num:
            result[stack[-1][1]] = num
            stack.pop()
        else:
            break
    stack.append((num, index))

print(*result)