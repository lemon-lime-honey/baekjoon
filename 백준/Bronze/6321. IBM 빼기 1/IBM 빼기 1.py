n = int(input())

for i in range(n):
    name = input()
    conversion = list()
    print(f'String #{i + 1}')

    for letter in name:
        temp = ord(letter)
        if temp == 90:
            conversion.append(chr(65))
        else:
            conversion.append(chr(temp + 1))
    
    print(f'{"".join(conversion)}\n')