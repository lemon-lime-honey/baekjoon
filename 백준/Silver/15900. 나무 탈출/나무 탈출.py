import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(point, parent, level):
    if len(tree[point]) == 1 and tree[point][0] == parent:
        global result
        result += level
        return

    for next_point in tree[point]:
        if next_point == parent: continue
        dfs(next_point, point, level + 1)


n = int(input())
tree = [[] for i in range(n + 1)]
result = 0

for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1, -1, 0)

print("Yes" if result % 2 else "No")
