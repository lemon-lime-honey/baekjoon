import sys
input = sys.stdin.readline


def getMax():
    global result

    for i in range(n):
        result = max(result, row(i), col(i))


def row(idx):
    res, cnt, color = 1, 1, colorDict[candy[idx][0]]

    for i in range(1, n):
        if colorDict[candy[idx][i]] == color:
            cnt += 1
        else:
            color = colorDict[candy[idx][i]]
            res = max(res, cnt)
            cnt = 1

    res = max(res, cnt)

    return res


def col(idx):
    res, cnt, color = 1, 1, colorDict[candy[0][idx]]

    for i in range(1, n):
        if colorDict[candy[i][idx]] == color:
            cnt += 1
        else:
            color = colorDict[candy[i][idx]]
            res = max(res, cnt)
            cnt = 1

    res = max(res, cnt)
    
    return res


n = int(input())
candy = [list(input().rstrip()) for i in range(n)]
colorDict = {'C': 0, 'P': 1, 'Z': 2, 'Y': 3}
result = 0

dr = [0, 0, -1, -1]
dc = [1, -1, 0, 0]

getMax()

for r in range(n):
    for c in range(n):
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 > nr or nr >= n or 0 > nc or nc >= n:
                continue
            if candy[r][c] != candy[nr][nc]:
                candy[r][c], candy[nr][nc] = candy[nr][nc], candy[r][c]
                getMax()
                candy[r][c], candy[nr][nc] = candy[nr][nc], candy[r][c]

print(result)
