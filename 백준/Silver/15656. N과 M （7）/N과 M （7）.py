def dfs():
    if len(arr) == m:
        print(*arr)
        return
    for i in range(n):
        arr.append(number[i])
        dfs()
        arr.pop()

n, m = map(int, input().split())
number = list(map(int, input().split()))
arr = list()
number.sort()

dfs()