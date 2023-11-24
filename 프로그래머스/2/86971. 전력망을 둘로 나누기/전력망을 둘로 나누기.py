def solution(n, wires):
    tree = [[] for i in range(n + 1)]
    answer = int(1e9)

    for start, end in wires:
        tree[start].append(end)
        tree[end].append(start)

    for start, end in wires:
        chk = [False for i in range(n + 1)]
        chk[1] = True
        stack = [1]
        cnt = 1

        while stack:
            now = stack.pop()
            for node in tree[now]:
                if ((now == start and node == end) or
                    (now == end and node == start) or
                    chk[node]):
                    continue
                stack.append(node)
                chk[node] = True
                cnt += 1

        answer = min(answer, abs(n - (2 * cnt)))

    return answer