import sys

n = int(sys.stdin.readline())
ipt = sys.stdin.readline().strip()
number = list()
stack = list()

for i in range(n):
    number.append(int(sys.stdin.readline()))


for element in ipt:
    if element.isalpha():
        stack.append(number[ord(element) - 65])
    elif element == '+':
        temp = stack.pop()
        temp += stack.pop()
        stack.append(temp)
    elif element == '-':
        temp = stack.pop()
        temp = stack.pop() - temp
        stack.append(temp)
    elif element == '*':
        temp = stack.pop()
        temp *= stack.pop()
        stack.append(temp)
    elif element == '/':
        temp = stack.pop()
        temp = stack.pop() / temp
        stack.append(temp)

print(f'{stack.pop():0.2f}')