from collections import deque
f, s, g, u, d = map(int, input().split())

que = deque([s])
visited = [1] + [0] * f
direction = [u, -1 * d]
visited[s] = 1
flag = False

while que:
    now = que.popleft()

    if now == g:
        break

    for i in range(2):
        new = now + direction[i]
        if (0 < new <= f) and not visited[new]:
            visited[new] = visited[now] + 1
            que.append(new)

if visited[g]:
    print(visited[g] - 1)
else:
    print('use the stairs')