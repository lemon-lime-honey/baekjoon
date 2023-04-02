import sys
input = sys.stdin.readline

def chk(n, r, c):
    ref = video[r][c]
    if n == 1:
        if ref: result.append(1)
        else: result.append(0)
        return
    flag = False
    for i in range(r, r + n):
        if flag: break
        for j in range(c, c + n):
            if video[i][j] != ref:
                flag = True
                break
    if flag:
        result.append('(')
        chk(n // 2, r, c)
        chk(n // 2, r, c + n // 2)
        chk(n // 2, r + n // 2, c)
        chk(n // 2, r + n // 2, c + n // 2)
        result.append(')')
    else:
        result.append(ref)

n = int(input())
video = [list(map(int, input().rstrip())) for i in range(n)]
result = list()
chk(n, 0, 0)
print(*result, sep='')