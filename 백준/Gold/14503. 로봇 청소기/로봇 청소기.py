import sys
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def clean(cleaner):
    global result
    r, c = cleaner[:2]
    if not room[r][c]:
        room[r][c] = 2
        result += 1
    chk = 0
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if (0 <= nr < n) and (0 <= nc < m):
            if not room[nr][nc]:
                chk += 1
    if chk:
        result += 1
        for i in range(4):
            if (cleaner[2] == 0):
                cleaner[2] = 3
                if not room[r][c - 1]:
                    room[r][c - 1] = 2
                    cleaner[:2] = r, c - 1
                    break
            elif (cleaner[2] == 1):
                cleaner[2] = 0
                if not room[r - 1][c]:
                    room[r - 1][c] = 2
                    cleaner[:2] = r - 1, c
                    break
            elif (cleaner[2] == 2):
                cleaner[2] = 1
                if not room[r][c + 1]:
                    room[r][c + 1] = 2
                    cleaner[:2] = r, c + 1
                    break
            elif (cleaner[2] == 3):
                cleaner[2] = 2
                if not room[r + 1][c]:
                    room[r + 1][c] = 2
                    cleaner[:2] = r + 1, c
                    break
    else:
        if (cleaner[2] == 0) and room[r + 1][c] != 1:
            cleaner[:2] = r + 1, c
        elif (cleaner[2] == 1) and room[r][c - 1] != 1:
            cleaner[:2] = r, c - 1
        elif (cleaner[2] == 2) and room[r - 1][c] != 1:
            cleaner[:2] = r - 1, c
        elif (cleaner[2] == 3) and room[r][c + 1] != 1:
            cleaner[:2] = r, c + 1
        else:
            return 1
    return 0


n, m = map(int, input().split())
cleaner = list(map(int, input().split()))
room = [list(map(int, input().split())) for i in range(n)]
result = 0

while True:
    temp = clean(cleaner)
    if temp: break

print(result)