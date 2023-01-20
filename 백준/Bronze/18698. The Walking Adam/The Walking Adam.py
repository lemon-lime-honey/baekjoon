t = int(input())

for i in range(t):
    movement = input()
    cnt = 0
    for move in movement:
        if move == 'U':
            cnt += 1
        if move == 'D':
            break
    print(cnt)