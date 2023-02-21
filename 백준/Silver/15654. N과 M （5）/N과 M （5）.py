def dfs():
    if len(arr) == m:
        print(*arr)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(number[i])
            dfs()
            arr.pop()
            visited[i] = False

n, m = map(int, input().split())
number = list(map(int, input().split()))
visited = [False for i in range(n)]
arr = list()
number.sort()

dfs()