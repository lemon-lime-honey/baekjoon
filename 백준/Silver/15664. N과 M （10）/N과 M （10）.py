def arr(offset):
    if len(target) == m:
        result.add(tuple(target))
        return
    for i in range(offset, n):
        if not visited[i]:
            visited[i] = True
            target.append(number[i])
            arr(i)
            target.pop()
            visited[i] = False


n, m = map(int, input().split())
visited = [False for i in range(n)]
number = sorted(list(map(int, input().split())))
target = list()
result = set()

arr(0)
for num in sorted(result):
    print(*num)