import sys
input = sys.stdin.readline


def draw(x, y, d, g):
    curve = [d]
    grid[y][x] = 1

    for i in range(g):
        for j in range(len(curve) - 1, -1, -1):
            curve.append((curve[j] + 1) % 4)

    for i in range(len(curve)):
        x, y = x + direction[curve[i]][1], y + direction[curve[i]][0]
        grid[y][x] = 1


direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]

n = int(input())
grid = [[0 for i in range(101)] for j in range(101)]
result = 0

for i in range(n):
    x, y, d, g = map(int, input().split())
    draw(x, y, d, g)

for i in range(100):
    for j in range(100):
        if (grid[i][j] == 1 and grid[i + 1][j + 1] == 1 and
            grid[i][j + 1] == 1 and grid[i + 1][j] == 1):
            result += 1

print(result)
