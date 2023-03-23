from collections import deque

n, k = map(int, input().split())
route = [[int(1e9), 0] for i in range(200001)]
route[n] = [0, 1]
que = deque([n])
answer = 0

while que:
    now = que.popleft()

    for i in [now - 1, now + 1, now * 2]:
        if (0 <= i < 200001):
            if route[i][0] == int(1e9):
                route[i][0] = route[now][0] + 1
                route[i][1] = route[now][1]
                que.append(i)
            elif route[i][0] == route[now][0] + 1:
                route[i][1] += route[now][1]

print(*route[k], sep='\n')