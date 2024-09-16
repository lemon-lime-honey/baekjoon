from itertools import combinations


def compare(p1, p2):
    cnt = 0
    for i in range(5):
        for j in range(7):
            if p1[i][j] != p2[i][j]:
                cnt += 1
    return cnt


n = int(input())
pictures = list()
result = [0, 0, int(1e9)]

for i in range(n):
    pictures.append([input() for i in range(5)])

comb = combinations(range(n), 2)

for n1, n2 in comb:
    chk = compare(pictures[n1], pictures[n2])
    if chk < result[2]:
        result = [n1, n2, chk]

print(result[0] + 1, result[1] + 1)
