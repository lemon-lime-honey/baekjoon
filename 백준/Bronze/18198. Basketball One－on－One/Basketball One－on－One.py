record = input()
a = 0
b = 0
ref = 0

while ref <= len(record)-2:
    if record[ref] == 'A':
        a += int(record[ref + 1])
    else:
        b += int(record[ref + 1])
    ref += 2

if a > b:
    print('A')
else:
    print('B')