import sys
input = sys.stdin.readline

def cnt(n, r, c):
    global minus, zero, one
    ref = paper[r][c]
    flag = False
    if n == 1:
        if ref == -1: minus += 1
        elif ref == 0: zero += 1
        elif ref == 1: one += 1
        return

    for i in range(r, n + r):
        if flag: break
        for j in range(c, n + c):
            if paper[i][j] != ref:
                flag = True
                break
    
    if flag:
        cnt(n // 3, r, c)
        cnt(n // 3, r, c + n // 3)
        cnt(n // 3, r + n // 3, c)
        cnt(n // 3, r, c + 2 * n // 3)
        cnt(n // 3, r + 2 * n // 3, c)
        cnt(n // 3, r + n // 3, c + n // 3)
        cnt(n // 3, r + n // 3, c + 2 * n // 3)
        cnt(n // 3, r + 2 * n // 3, c + n // 3)
        cnt(n // 3, r + 2 * n // 3, c + 2 * n // 3)

    else:
        if ref == -1: minus += 1
        elif ref == 0: zero += 1
        elif ref == 1: one += 1
        return

n = int(input())
paper = [list(map(int, input().split())) for i in range(n)]
minus, zero, one = 0, 0, 0
cnt(n, 0, 0)
print(minus, zero, one, sep='\n')