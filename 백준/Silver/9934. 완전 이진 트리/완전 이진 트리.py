def get_tree(initial, final, depth):
    if initial == final:
        tree[depth].append(order[final])
        return

    root = (initial + final) // 2
    tree[depth].append(order[root])
    get_tree(initial, root - 1, depth + 1)
    get_tree(root + 1, final, depth + 1)


k = int(input())
order = list(map(int, input().split()))
tree = [[] for i in range(k)]

get_tree(0, len(order) - 1, 0)

for branch in tree:
    print(*branch)