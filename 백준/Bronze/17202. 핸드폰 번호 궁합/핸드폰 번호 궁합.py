from collections import deque

a = input()
b = input()
temp = deque()

for i in range(8):
    temp.append(int(a[i]))
    temp.append(int(b[i]))

temp.append('/')

while True:
    num1 = temp.popleft()
    num2 = temp.popleft()
    if num2 == '/':
        temp.append(num2)
    else:
        temp.append((num1 + num2) % 10)
        temp.appendleft(num2)
    if len(temp) == 3:
        print(temp[0], temp[1], sep = '')
        break