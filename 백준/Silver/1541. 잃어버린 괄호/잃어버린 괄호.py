eq = input()
temp = list()
element = list()
result = 0
num = 0
flag = 0

for letter in eq:
    if letter.isdigit():
        temp.append(letter)
    else:
        element.append(''.join(temp))
        temp = list()
        element.append(letter)
element.append(''.join(temp))

for item in element:
    if item == '-':
        result -= num
        num = 0
        flag = 1
    elif item == '+':
        continue
    else:
        if flag == 0:
            result += int(item)
        else:
            num += int(item)

if (flag == 1) * (num != 0):
    result -= num

print(result)