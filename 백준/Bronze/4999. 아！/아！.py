a = input()
b = input()

countA = 0
countB = 0

for letter in a:
    if letter == 'a':
        countA += 1

for letter in b:
    if letter == 'a':
        countB += 1

if countA >= countB:
    print('go')
else:
    print('no')