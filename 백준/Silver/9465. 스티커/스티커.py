import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for j in range(2)]
    result = [[0 for j in range(n + 2)] for k in range(2)]

    for j in range(2, n + 2):
        result[0][j] = max(result[1][j - 1], result[1][j - 2]) + sticker[0][j - 2]
        result[1][j] = max(result[0][j - 1], result[0][j - 2]) + sticker[1][j - 2]
    
    print(max(result[0][-1], result[1][-1]))