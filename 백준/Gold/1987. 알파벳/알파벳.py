dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def dfs(r, c, cnt):
    global result
    result = max(result, cnt)

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if (0 <= nr < r_ipt) and (0 <= nc < c_ipt):
            if not alphabet[ord(board[nr][nc]) - 65] and not visited[nr][nc]:
                alphabet[ord(board[nr][nc]) - 65] = True
                visited[nr][nc] = True
                dfs(nr, nc, cnt + 1)
                visited[nr][nc] = False
                alphabet[ord(board[nr][nc]) - 65] = False

r_ipt, c_ipt = map(int, input().split())
visited = [[False for i in range(c_ipt)] for j in range(r_ipt)]
alphabet = [False] * 26
board = list()

for i in range(r_ipt):
    board.append(list(input()))

visited[0][0] = True
alphabet[ord(board[0][0]) - 65] = True
result = 1

dfs(0, 0, result)
print(result)