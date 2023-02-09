t = int(input())

for i in range(t):
    chess = list()
    rook_col = set()
    rook_row = set()
    rook_cnt = 0

    for j in range(8):
        chess.append(list(input()))

        for k in range(8):
            if chess[j][k] == 'O':
                rook_col.add(k)
                rook_row.add(j)
                rook_cnt += 1
    
    if len(rook_col) == len(rook_row) == rook_cnt == 8:
        print(f'#{i + 1} yes')
    else:
        print(f'#{i + 1} no')