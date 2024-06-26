def backtrack(total, route):
    if total == n:
        global cnt
        cnt += 1
        if cnt == k:
            global result
            result = '+'.join(route)
        return
    for i in range(1, 4):
        if total + i <= n:
            route.append(str(i))
            backtrack(total + i, route)
            route.pop()

n, k = map(int, input().split())
result = None
cnt = 0
backtrack(0, list())

print(result if result else -1)
