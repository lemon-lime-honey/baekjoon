from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [0 for i in range(101)]
chk = [int(1e9) for i in range(101)]
chk[1] = 0
que = deque([1])

for i in range(n + m):
    a, b = map(int, input().split())
    board[a] = b

while que:
    now = que.popleft()

    for i in range(1, 7):
        point = now + i
        if (0 < point < 101):
            if board[point]:
                point = board[now + i]
            if chk[now] + 1 < chk[point]:
                chk[point] = chk[now] + 1
                que.append(point)

print(chk[100])