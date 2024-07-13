import sys
input = sys.stdin.readline


def solve(days, total, before):
    if days == n:
        if total >= m:
            global result
            result += 1
        return
    for i in range(3):
        if i != before:
            solve(days + 1, total + points[0][i], i)
            solve(days + 1, total + points[1][i], i)
        else:
            solve(days + 1, total + points[0][i] // 2, i)
            solve(days + 1, total + points[1][i] // 2, i)


n, m = map(int, input().split())
points = [list(map(int, input().split())) for i in range(2)]
result = 0

solve(0, 0, 5)
print(result)
