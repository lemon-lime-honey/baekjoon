import sys
input = sys.stdin.readline


def get():
    result = x

    while result <= m * n:
        if (result - x) % m == 0 and (result - y) % n == 0:
            return result
        result += m

    return -1


t = int(input())

for i in range(t):
    m, n, x, y = map(int, input().split())
    print(get())