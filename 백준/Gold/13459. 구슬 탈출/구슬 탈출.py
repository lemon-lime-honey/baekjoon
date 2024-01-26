from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    que = deque()
    chk = set()
    que.append(tuple(balls))
    chk.add(tuple(balls[:-1]))

    while que:
        br, bc, rr, rc, mv = que.popleft()
        if mv >= 10:
            return 0

        for i in range(4):
            nbr, nbc, bmv = move(br, bc, i)
            nrr, nrc, rmv = move(rr, rc, i)

            if board[nbr][nbc] != 'O':
                if board[nrr][nrc] == 'O':
                    return 1

                if nbr == nrr and nbc == nrc:
                    if bmv <= rmv:
                        nrr, nrc = nrr - dr[i], nrc - dc[i]
                    else:
                        nbr, nbc = nbr - dr[i], nbc - dc[i]

                if (nbr, nbc, nrr, nrc) in chk: continue
                chk.add((nbr, nbc, nrr, nrc))
                que.append((nbr, nbc, nrr, nrc, mv + 1))

    return 0


def move(r, c, idx):
    mv = 0

    while board[r + dr[idx]][c + dc[idx]] != '#' and board[r][c] != 'O':
        r += dr[idx]
        c += dc[idx]
        mv += 1

    return (r, c, mv)


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n, m = map(int, input().split())
board = list()

balls = [0, 0, 0, 0, 0]

for i in range(n):
    board.append(input().rstrip())
    for j in range(m):
        if board[i][j] == 'B':
            balls[: 2] = [i, j]
        elif board[i][j] == 'R':
            balls[2: 4] = [i, j]

print(bfs())