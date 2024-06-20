import sys
sys.setrecursionlimit(int(1e9))

def solution(nodeinfo):
    def solve(node):
        if not node: return
        root = [-1, 0, 0]
        for i in range(len(node)):
            if root[0] < node[i][1]:
                root = [node[i][1], node[i][2], i]
        answer[0].append(root[1])
        solve(node[:root[2]])
        solve(node[root[2] + 1:])
        answer[1].append(root[1])


    nodes = list()

    for i in range(len(nodeinfo)):
        nodes.append((nodeinfo[i][0], nodeinfo[i][1], i + 1))

    nodes.sort(key=lambda x: x[0])
    answer = [[], []]

    solve(nodes)

    return answer