import sys
input = sys.stdin.readline

k = int(input())

for i in range(k):
    v, e = map(int, input().split())
    visited = [0 for j in range(v + 1)]
    graph = [[] for j in range(v + 1)]
    flag = True

    for j in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for j in range(1, v + 1):
        if visited[j]: continue

        stack = [j]
        visited[j] = 1

        while stack:
            node = stack.pop()
            for next_node in graph[node]:
                if not visited[next_node]:
                    if visited[node] == 1:
                        visited[next_node] = 2
                    else:
                        visited[next_node] = 1
                    stack.append(next_node)

    for node in range(1, v + 1):
        for next_node in graph[node]:
            if visited[node] == visited[next_node]:
                flag = False
                break
        if not flag:
            print('NO')
            break
    else:
        print('YES')
