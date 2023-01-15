string = input()
happy = 0
sad = 0
cnt = 0
before = True

for letter in string:
    if letter == ':':
        cnt = 1
        before = True
    elif (letter == '-') and (cnt == 1) and before:
        cnt = 2
    elif (letter == '(') and (cnt == 2) and before:
        sad += 1
    elif (letter == ')') and (cnt == 2) and before:
        happy += 1
    else:
        cnt = 0
        before = False

if happy == sad == 0:
    print('none')
elif happy == sad:
    print('unsure')
elif happy > sad:
    print('happy')
else:
    print('sad')