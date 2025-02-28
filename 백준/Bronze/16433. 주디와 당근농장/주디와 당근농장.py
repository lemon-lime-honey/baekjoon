n, r, c = map(int, input().split())
result = [["." for i in range(n)] for j in range(n)]
r -= 1
c -= 1

for i in range(n):
    for j in range(n):
        if (i % 2 == r % 2 and j % 2 == c % 2) or (i % 2 != r % 2 and j % 2 != c % 2):
            result[i][j] = "v"

for line in result:
    print(*line, sep="")
