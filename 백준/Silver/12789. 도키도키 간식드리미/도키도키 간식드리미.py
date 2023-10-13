import sys
input = sys.stdin.readline

n = int(input())
students = list(map(int, input().split()))
stack = list()
target = 1

for i in range(n):
    stack.append(students[i])

    while stack and stack[-1] == target:
        stack.pop()
        target += 1

    if len(stack) > 1 and stack[-2] < stack[-1]:
        print('Sad')
        break
else:
    print('Nice' if not stack else 'Sad')