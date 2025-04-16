n, m = map(int, input().split())
points = list()

for i in range(n):
    ipt = list(map(int, input().split()))
    for j in range(m):
        if ipt[j]:
            points.append((i, j))

print(abs(points[1][0] - points[0][0]) + abs(points[1][1] - points[0][1]))
