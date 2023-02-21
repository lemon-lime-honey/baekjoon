def dfs(offset):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(offset, n):
        arr.append(number[i])
        dfs(i)
        arr.pop()

n, m = map(int, input().split())
number = list(map(int, input().split()))
arr = list()
number.sort()

dfs(0)