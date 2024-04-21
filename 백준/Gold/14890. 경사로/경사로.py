import sys
input = sys.stdin.readline


def vertical(num):
    bridge = [False for i in range(n)]
    for i in range(1, n):
        if abs(maps[i][num] - maps[i - 1][num]) > 1: return False
        if maps[i][num] == maps[i - 1][num]: continue
        if maps[i][num] > maps[i - 1][num]:
            for j in range(l):
                if (i - j - 1 < 0 or
                    maps[i - 1][num] != maps[i - j - 1][num] or
                    bridge[i - j - 1]):
                    return False
                bridge[i - j - 1] = True
        if maps[i][num] < maps[i - 1][num]:
            for j in range(l):
                if (i + j >= n or
                    maps[i + j][num] != maps[i][num] or
                    bridge[i + j]):
                    return False
                bridge[i + j] = True
    return True


def horizontal(num):
    bridge = [False for i in range(n)]
    for i in range(1, n):
        if abs(maps[num][i] - maps[num][i - 1]) > 1: return False
        if maps[num][i] == maps[num][i - 1]: continue
        if maps[num][i] > maps[num][i - 1]:
            for j in range(l):
                if (i - j - 1 < 0 or
                    maps[num][i - 1] != maps[num][i - j - 1] or
                    bridge[i - j - 1]):
                    return False
                bridge[i - j - 1] = True
        if maps[num][i] < maps[num][i - 1]:
            for j in range(l):
                if (i + j >= n or
                    maps[num][i + j] != maps[num][i] or
                    bridge[i + j]):
                    return False
                bridge[i + j] = True
    return True


n, l = map(int, input().split())
maps = [list(map(int, input().split())) for i in range(n)]
result = 0

for i in range(n):
    if vertical(i): result += 1
    if horizontal(i): result += 1

print(result)