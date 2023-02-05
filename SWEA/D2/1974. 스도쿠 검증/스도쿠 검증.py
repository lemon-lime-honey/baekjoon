t = int(input())

for i in range(t):
    puzzle = [[0 for j in range(9)]for k in range(9)]
    flag = True
    print(f'#{i + 1}', end = ' ')

    for j in range(9):
        puzzle[j] = list(map(int, input().split()))
    
    for j in range(9):
        num = set()
        for k in range(9):
            num.add(puzzle[j][k])
        if len(num) != 9:
            flag = False

    if flag:
        for j in range(9):
            num = set()
            for k in range(9):
                num.add(puzzle[k][j])
            if len(num) != 9:
                flag = False

    if flag:
        for j in range(0, 9, 3):
            for k in range(0, 9, 3):
                num = set()
                for l in range(3):
                    for m in range(3):
                        num.add(puzzle[j + l][k + m])
                if len(num) != 9:
                    flag = False
    
    if flag:
        print(1)
    else:
        print(0)