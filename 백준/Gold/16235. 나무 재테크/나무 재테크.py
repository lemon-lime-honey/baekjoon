import sys
input = sys.stdin.readline


def spring_summer():
    for i in range(n):
        for j in range(n):
            length = len(tree[i][j])
            tree[i][j].sort()

            for l in range(length):
                if tree[i][j][l] <= nutrient[i][j]:
                    nutrient[i][j] -= tree[i][j][l]
                    tree[i][j][l] += 1
                else:
                    for t in tree[i][j][l:]:
                        nutrient[i][j] += t // 2
                    tree[i][j] = tree[i][j][:l]
                    break


def autumn():
    for i in range(n):
        for j in range(n):
            for t in tree[i][j]:
                if t % 5 == 0:
                    for l in range(8):
                        ni, nj = i + di[l], j + dj[l]
                        if not (0 <= ni < n and 0 <= nj < n):
                            continue
                        tree[ni][nj].append(1)


def winter():
    for i in range(n):
        for j in range(n):
            nutrient[i][j] += a[i][j]


di = [0, 0, -1, -1, -1, 1, 1, 1]
dj = [1, -1, 0, 1, -1, 0, 1, -1]

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
tree = [[[] for i in range(n)] for j in range(n)]
nutrient = [[5 for i in range(n)] for j in range(n)]

for i in range(m):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

for i in range(k):
    spring_summer()
    autumn()
    winter()

result = 0

for i in range(n):
    for j in range(n):
        result += len(tree[i][j])

print(result)