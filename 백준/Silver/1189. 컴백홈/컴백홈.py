def backtrack(row, col, cnt):
    global result
    if row == 0 and col == c:
        if cnt == k:
            result += 1
        return
    for i in range(4):
        nr, nc = row + dr[i], col + dc[i]
        if (nr < 0 or nr > r or
            nc < 0 or nc > c or
            (nr, nc) in visited or
            board[nr][nc] == 'T'):
            continue
        visited.add((nr, nc))
        backtrack(nr, nc, cnt + 1)
        visited.discard((nr, nc))


dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]

r, c, k = map(int, input().split())
board = [input() for i in range(r)]
r -= 1
c -= 1
result = 0

visited = {(r, 0)}
backtrack(r, 0, 1)

print(result)