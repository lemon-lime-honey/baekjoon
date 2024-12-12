import sys

input = sys.stdin.readline

n, k = map(int, input().split())
obstacles = set(tuple(map(int, input().split())) for i in range(n))
command = input().rstrip()

x, y = 0, 0

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for letter in command:
    match letter:
        case "U":
            x += d[0][0]
            y += d[0][1]
            if (x, y) in obstacles:
                x -= d[0][0]
                y -= d[0][1]
        case "D":
            x += d[1][0]
            y += d[1][1]
            if (x, y) in obstacles:
                x -= d[1][0]
                y -= d[1][1]
        case "R":
            x += d[2][0]
            y += d[2][1]
            if (x, y) in obstacles:
                x -= d[2][0]
                y -= d[2][1]
        case "L":
            x += d[3][0]
            y += d[3][1]
            if (x, y) in obstacles:
                x -= d[3][0]
                y -= d[3][1]

print(x, y)
