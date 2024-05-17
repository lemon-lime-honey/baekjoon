from collections import deque

n = int(input())
que = deque([(1, 0, 0)])
arr = [[int(1e9) for i in range(n * 2 + 1)] for j in range(n * 2 + 1)]
arr[1][0] = 0

while que:
    now, clipboard, cnt = que.popleft()
    if now == n: break
    if clipboard and now + clipboard <= n * 2 and cnt + 1 < arr[now + clipboard][clipboard]:
        arr[now + clipboard][clipboard] = cnt + 1
        que.append((now + clipboard, clipboard, cnt + 1))
    if now > 1 and cnt + 1 < arr[now - 1][clipboard]:
        arr[now - 1][clipboard] = cnt + 1
        que.append((now - 1, clipboard, cnt + 1))
    que.append((now, now, cnt + 1))

print(min(arr[n]))