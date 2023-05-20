import sys
input = sys.stdin.readline


def find(p):
    if p != chk[p]:
        chk[p] = find(chk[p])
    return chk[p]


def union(p1, p2):
    p1, p2 = find(p1), find(p2)
    if p1 == p2:
        return True
    if p1 < p2: chk[p2] = p1
    else: chk[p1] = p2
    return False


n, m = map(int, input().split())
chk = [i for i in range(n)]
result = -1

for i in range(m):
    a, b = map(int, input().split())
    flag = union(a, b)
    if flag and result == -1:
        result = i + 1

print(0 if result == -1 else result)