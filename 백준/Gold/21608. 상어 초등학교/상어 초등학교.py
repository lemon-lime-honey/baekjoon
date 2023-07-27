from collections import defaultdict
import sys
input = sys.stdin.readline


point = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def find(s):
    empty = defaultdict(list)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if seat[i][j] == 0:
                chk1 = 0
                chk2 = 0
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if (0 < nr < n + 1) and (0 < nc < n + 1):
                        if seat[nr][nc] in student[s]:
                            chk1 += 1
                        elif seat[nr][nc] == 0:
                            chk2 += 1
                empty[(i, j)].extend([chk1, chk2])
    targets = sorted(empty.items(), key=lambda x: (-x[1][0], -x[1][1], x[0][0], x[0][1]))
    seat[targets[0][0][0]][targets[0][0][1]] = s


n = int(input())
student = defaultdict(set)
student_list = list()
seat = [[0 for i in range(n + 1)] for j in range(n + 1)]
satis = [[0 for i in range(n + 1)] for j in range(n + 1)]

for i in range(n ** 2):
    ipt = list(map(int, input().split()))
    student[ipt[0]] = set(ipt[1:])
    student_list.append(ipt[0])

for s in student_list:
    find(s)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        cnt = 0
        for k in range(4):
            nr, nc = i + dr[k], j + dc[k]
            if (0 < nr < n + 1) and (0 < nc < n + 1):
                if seat[nr][nc] in student[seat[i][j]]:
                    cnt += 1
        satis[i][j] = point[cnt]

print(sum(map(sum, satis)))