from collections import deque

dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

t = int(input())

for i in range(t):
    l = int(input())
    r, c = map(int, input().split())
    tr, tc = map(int, input().split())
    chess = [[0 for j in range(l)] for k in range(l)]

    que = deque([[r, c]])

    while que:
        now = que.popleft()
        if (now[0] == tr) and (now[1] == tc):
            break

        for j in range(8):
            del_r = now[0] + dr[j]
            del_c = now[1] + dc[j]
            if (0 <= del_r < l) and (0 <= del_c <l) and not chess[del_r][del_c]:
                que.append([del_r, del_c])
                chess[del_r][del_c] = chess[now[0]][now[1]] + 1
    
    print(chess[tr][tc])
