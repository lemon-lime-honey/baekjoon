import heapq, sys
input = sys.stdin.readline


def pooling(row, col, size):
    if size == 1:
        return board[row][col]
    a = pooling(row, col, size//2)
    b = pooling(row, col+size//2, size//2)
    c = pooling(row + size//2, col, size//2)
    d = pooling(row+size//2, col+size//2, size//2)
    result = sorted([a, b, c, d])
    return result[2]


n = int(input())
board = [list(map(int, input().split())) for i in range(n)]
print(pooling(0, 0, n))