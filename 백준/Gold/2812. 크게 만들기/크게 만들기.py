n, k = map(int, input().split())
number = input()
stack = list()
cnt = 0

for i in range(n):
    while cnt < k and stack and int(stack[-1]) < int(number[i]):
        stack.pop()
        cnt += 1
    stack.append(number[i])

while stack and cnt < k:
    stack.pop()
    cnt += 1

print(''.join(stack))