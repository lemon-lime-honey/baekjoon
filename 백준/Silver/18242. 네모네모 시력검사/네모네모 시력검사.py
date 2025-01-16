import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [input().rstrip() for i in range(n)]

left, right = None, None

for i in range(n):
    for j in range(m):
        if graph[i][j] == "#":
            left = (i, j)
            break
    if left:
        break

for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if graph[i][j] == "#":
            right = (i, j)
            break
    if right:
        break

if graph[left[0]][(left[1] + right[1]) // 2] == ".":
    print("UP")
elif graph[right[0]][(left[1] + right[1]) // 2] == ".":
    print("DOWN")
elif graph[(left[0] + right[0]) // 2][left[1]] == ".":
    print("LEFT")
elif graph[(left[0] + right[0]) // 2][right[1]] == ".":
    print("RIGHT")
