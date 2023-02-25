n = int(input())
winner = True
turn = True

while n:
    if turn:
        winner = True
        turn = False
        if n > 3:
            n -= 3
        else:
            n -= 1
    else:
        winner = False
        turn = True
        if n > 3:
            n -= 3
        else:
            n -= 1

if winner:
    print('SK')
else:
    print('CY')