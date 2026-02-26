import sys

sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]

    mid = (start + end) // 2
    _left = init(node * 2, start, mid)
    _right = init(node * 2 + 1, mid + 1, end)

    tree[node] = _left + _right

    return tree[node]


def update(node, start, end, index, value):
    if index < start or index > end:
        return

    if start == end:
        tree[node] = value
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, index, value)
    update(node * 2 + 1, mid + 1, end, index, value)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(node, start, end, left, right):
    if left > end or right < start:
        return 0

    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2
    _left = query(node * 2, start, mid, left, right)
    _right = query(node * 2 + 1, mid + 1, end, left, right)

    return _left + _right


if __name__ == "__main__":
    n, q = map(int, input().split())
    nums = list(map(int, input().split()))
    tree = [0 for i in range(4 * n + 1)]
    result = list()

    init(1, 0, n - 1)

    for i in range(q):
        x, y, a, b = map(int, input().split())

        result.append(query(1, 0, n - 1, min(x, y) - 1, max(x, y) - 1))
        update(1, 0, n - 1, a - 1, b)

    print(*result, sep="\n")
