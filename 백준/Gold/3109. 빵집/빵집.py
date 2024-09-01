import sys
input = sys.stdin.readline


def chk(r, c):
    maps[r][c] = 'x'
    if c == col - 1:
        return True
    if r > 0 and maps[r - 1][c + 1] == '.':
        if chk(r - 1, c + 1): return True
    if maps[r][c + 1] == '.':
        if chk(r, c + 1): return True
    if r + 1 < row and maps[r + 1][c + 1] == '.':
        if chk(r + 1, c + 1): return True
    return False


row, col = map(int, input().split())
maps = [list(input().rstrip()) for i in range(row)]
result = 0

for i in range(row):
    if chk(i, 0):
        result += 1

print(result)
