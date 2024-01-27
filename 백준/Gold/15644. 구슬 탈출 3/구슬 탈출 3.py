from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    mvmt = deque()
    que = deque()
    chk = set()
    mvmt.append('')
    que.append(tuple(balls))
    chk.add(tuple(balls[:-1]))

    while que:
        br, bc, rr, rc, mv = que.popleft()
        movement = mvmt.popleft()
        if mv >= 10:
            print(-1)
            return

        for i in range(4):
            nbr, nbc, bmv = move(br, bc, i)
            nrr, nrc, rmv = move(rr, rc, i)

            if board[nbr][nbc] != 'O':
                if board[nrr][nrc] == 'O':
                    print(mv + 1)
                    print(movement + d[i])
                    return

                if nbr == nrr and nbc == nrc:
                    if bmv <= rmv:
                        nrr, nrc = nrr - dr[i], nrc - dc[i]
                    else:
                        nbr, nbc = nbr - dr[i], nbc - dc[i]

                if (nbr, nbc, nrr, nrc) in chk: continue
                mvmt.append(movement + d[i])
                chk.add((nbr, nbc, nrr, nrc))
                que.append((nbr, nbc, nrr, nrc, mv + 1))

    print(-1)


def move(r, c, idx):
    mv = 0

    while board[r + dr[idx]][c + dc[idx]] != '#' and board[r][c] != 'O':
        r += dr[idx]
        c += dc[idx]
        mv += 1

    return (r, c, mv)


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
d = 'RLUD'

n, m = map(int, input().split())
balls = [0, 0, 0, 0, 0]
board = list()

for i in range(n):
    board.append(input().rstrip())
    for j in range(m):
        if board[i][j] == 'B':
            balls[0: 2] = [i, j]
        elif board[i][j] == 'R':
            balls[2: 4] = [i, j]

bfs()