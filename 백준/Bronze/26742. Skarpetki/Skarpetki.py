ipt = input()
b = 0
c = 0

for color in ipt:
    if color == 'B':
        b += 1
    else:
        c += 1

print(b // 2 + c // 2)