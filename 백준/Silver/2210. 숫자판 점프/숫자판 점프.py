import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))


def dfs(r, c):
    if len(temp) == 6:
        result.add(''.join(temp))
        return

    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nr, nc = r + dr, c + dc
        if (nr < 0 or nc < 0 or nr > 4 or nc > 4):
            continue
        temp.append(board[nr][nc])
        dfs(nr, nc)
        temp.pop()


board = [input().rstrip().split() for i in range(5)]
result = set()
temp = list()

for i in range(5):
    for j in range(5):
        temp.append(board[i][j])
        dfs(i, j)
        temp.pop()

print(len(result))