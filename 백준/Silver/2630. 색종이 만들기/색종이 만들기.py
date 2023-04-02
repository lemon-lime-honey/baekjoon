import sys
input = sys.stdin.readline

def cnt(n, r, c):
    global blue, white
    ref = paper[r][c]
    flag = False
    if n == 1:
        if ref: blue += 1
        else: white += 1
        return

    for i in range(r, n + r):
        if flag: break
        for j in range(c, n + c):
            if paper[i][j] != ref:
                flag = True
                break
    
    if flag:
        cnt(n // 2, r, c)
        cnt(n // 2, r, c + n // 2)
        cnt(n // 2, r + n // 2, c)
        cnt(n // 2, r + n // 2, c + n // 2)
    else:
        if ref: blue += 1
        else: white += 1

n = int(input())
paper = [list(map(int, input().split())) for i in range(n)]
blue, white = 0, 0
cnt(n, 0, 0)
print(white, blue, sep='\n')