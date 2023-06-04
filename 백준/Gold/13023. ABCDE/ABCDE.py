import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(p, length):
    global flag
    chk[p] = True
    if length == 4:
        flag = True
        return
    for person in relationship[p]:
        if not chk[person]:
            chk[person] = True
            dfs(person, length + 1)
            chk[person] = False


n, m = map(int, input().split())
relationship = [[] for i in range(n)]
chk = [False for i in range(n)]
flag = False

for i in range(m):
    a, b = map(int, input().split())
    relationship[a].append(b)
    relationship[b].append(a)

for i in range(n):
    dfs(i, 0)
    chk[i] = False
    if flag: break

print(1 if flag else 0)