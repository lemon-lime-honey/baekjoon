ipt = input()
total = 0

for index, element in enumerate(ipt):
    if element.isdigit():
        if index != 8:
            total += int(element)
        else:
            if total == int(element):
                print('YES')
            else:
                print('NO')