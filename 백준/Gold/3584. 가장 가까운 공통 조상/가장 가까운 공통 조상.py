import sys
input = sys.stdin.readline


def dfs(point):
    visited = [False for i in range(n + 1)]
    visited[point] = True
    stack = [point]
    result = [point]
    while stack:
        now = stack.pop()
        if not visited[tree[now]]:
            visited[tree[now]] = True
            result.append(tree[now])
            stack.append(tree[now])
    return result


t = int(input())

for i in range(t):
    n = int(input())
    tree = [0 for j in range(n + 1)]
    stack = list()

    for j in range(n - 1):
        a, b = map(int, input().split())
        tree[b] = a
    
    target1, target2 = map(int, input().split())
    result1 = dfs(target1)
    result2 = dfs(target2)

    while result1 and result2 and (result1[-1] == result2[-1]):
        answer = result1.pop()
        result2.pop()

    print(answer)