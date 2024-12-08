import sys

input = sys.stdin.readline


def get_type(r, c):
    if state[r + 3][c] == "*":
        return 4
    if state[r + 2][c] == "*":
        return 3
    if state[r + 1][c] == "*":
        return 2
    if state[r][c] == "*":
        return 1
    return 0


result = [0 for i in range(5)]

m, n = map(int, input().split())
state = [input().rstrip() for i in range(5 * m + 1)]

for i in range(1, 5 * m + 1, 5):
    for j in range(1, 5 * n + 1, 5):
        result[get_type(i, j)] += 1

print(*result)
