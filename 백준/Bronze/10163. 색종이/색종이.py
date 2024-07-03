n = int(input())
paper = [[0 for i in range(1002)] for j in range(1002)]
result = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    r, c, h, w = map(int, input().split())
    for j in range(r, r + h):
        for k in range(c, c + w):
            paper[j][k] = i

for i in range(1002):
    for j in range(1002):
        result[paper[i][j]] += 1

print(*result[1:], sep='\n')
