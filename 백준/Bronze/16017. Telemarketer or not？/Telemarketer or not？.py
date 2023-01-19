number = list()

for i in range(4):
    number.append(int(input()))

if (number[0] in (8, 9)) * (number[3] in (8, 9)) * (number[1] == number[2]):
    print('ignore')
else:
    print('answer')