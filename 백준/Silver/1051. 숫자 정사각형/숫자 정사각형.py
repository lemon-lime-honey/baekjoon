def find(s):
    while True:
        for i in range(n - s + 1):
            for j in range(m - s + 1):
                if rect[i][j] == rect[i + s - 1][j] == rect[i][j + s - 1] == rect[i + s - 1][j + s - 1]:
                    return s
        s -= 1

n, m = map(int, input().split())
rect = [[0 for i in range(m)]for j in range(n)]

for i in range(n):
    rect[i] = list(map(int, input()))

side = min(m, n)
print(find(side) ** 2)