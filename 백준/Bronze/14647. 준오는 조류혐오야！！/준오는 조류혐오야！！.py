n, m = map(int, input().split())
nine_total = 0
nine_max = 0

board = [input().split() for i in range(n)]

for i in range(n):
    nine = 0
    for j in range(m):
        nine += board[i][j].count("9")
    nine_total += nine
    nine_max = max(nine_max, nine)

for i in range(m):
    nine = 0
    for j in range(n):
        nine += board[j][i].count("9")
    nine_max = max(nine_max, nine)

print(nine_total - nine_max)
