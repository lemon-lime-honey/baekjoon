import sys

sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline


def update(node, start, end, index, value):
    if start > index or end < index:
        return
    if start == end:
        tree[node] += value
        return

    mid = (start + end) // 2

    update(node * 2, start, mid, index, value)
    update(node * 2 + 1, mid + 1, end, index, value)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if start >= left and right >= end:
        return tree[node]

    mid = (start + end) // 2

    _left = query(node * 2, start, mid, left, right)
    _right = query(node * 2 + 1, mid + 1, end, left, right)

    return _left + _right


if __name__ == "__main__":
    n, q = map(int, input().split())
    tree = [0 for i in range(4 * n)]
    result = list()

    for i in range(q):
        a, b, c = map(int, input().split())

        if a == 1:
            update(1, 0, n - 1, b - 1, c)
        elif a == 2:
            result.append(query(1, 0, n - 1, b - 1, c - 1))

    print(*result, sep="\n")
