import sys
input = sys.stdin.readline

n = int(input())
ipt = input().rstrip()

maps = [[0 for i in range(101)] for j in range(101)]
direction = ((1, 0), (0, -1), (-1, 0), (0, 1))
maps[50][50] = 1
pos = [50, 50]
d = 0

for m in ipt:
    if m == 'F':
        pos = [pos[0] + direction[d][0], pos[1] + direction[d][1]]
        maps[pos[0]][pos[1]] = 1
    elif m == 'R':
        d = (d + 1) % 4
    else:
        d = (d - 1) % 4

rlo, rhi, clo, chi = 100, 0, 100, 0

for i in range(101):
    for j in range(101):
        if maps[i][j] == 1:
            rlo = min(rlo, i)
            rhi = max(rhi, i)
            clo = min(clo, j)
            chi = max(chi, j)

result = list()

for i in range(rlo, rhi + 1):
    temp = list()
    for j in range(clo, chi + 1):
        if maps[i][j] == 0:
            temp.append('#')
        else:
            temp.append('.')
    result.append(''.join(temp))

print(*result, sep='\n')
