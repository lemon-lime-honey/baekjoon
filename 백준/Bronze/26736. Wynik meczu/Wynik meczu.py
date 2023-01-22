ipt = input()
a = 0
b = 0

for letter in ipt:
    if letter == 'A':
        a += 1
    else:
        b += 1

print(f'{a} : {b}')