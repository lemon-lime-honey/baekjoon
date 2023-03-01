n = int(input())
number = list()

for i in range(n):
    ipt = input()
    temp = list()

    for index, element in enumerate(ipt):
        if element.isdigit():
            temp.append(element)
            if index == (len(ipt) - 1):
                number.append(int(''.join(temp)))
        else:
            if temp:
                number.append(int(''.join(temp)))
                temp = list()
                
number.sort()
print(*number, sep='\n')