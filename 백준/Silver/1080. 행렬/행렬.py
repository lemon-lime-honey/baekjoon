import sys
input = sys.stdin.readline


def flip(r, c):
    for i in range(3):
        for j in range(3):
            a[r + i][c + j] = 0 if a[r + i][c + j] else 1


n, m = map(int, input().split())
a = [list(map(int, list(input().rstrip()))) for i in range(n)]
b = [list(map(int, list(input().rstrip()))) for i in range(n)]

if (n < 3 or m < 3) and a != b:
    print(-1)
    sys.exit()

result = 0

for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            result += 1
            flip(i, j)

print(result if a == b else -1)
