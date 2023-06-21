import sys
input = sys.stdin.readline


def find(s):
    if s != school[s]:
        school[s] = find(school[s])
    return school[s]


def union(s1, s2):
    s1, s2 = find(s1), find(s2)
    if s1 == s2: return True
    if s1 < s2: school[s2] = s1
    else: school[s1] = s2
    return False


n, m = map(int, input().split())
mw = list(map(str, input().strip().split()))
school = [i for i in range(n)]
routes = [list(map(int, input().split())) for i in range(m)]
routes.sort(key=lambda x:x[2])
result = 0

for u, v, d in routes:
    if mw[u - 1] != mw[v - 1]:
        chk = union(u - 1, v - 1)
        if not chk: result += d

for i in range(1, n):
    if find(i) != find(i - 1):
        print(-1)
        break
else:
    print(result)