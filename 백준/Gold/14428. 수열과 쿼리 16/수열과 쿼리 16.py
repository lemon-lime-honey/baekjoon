import sys

sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = start
        return tree[node]

    mid = (start + end) // 2

    _left = init(node * 2, start, mid)
    _right = init(node * 2 + 1, mid + 1, end)

    if nums[_left] <= nums[_right]:
        tree[node] = _left
    else:
        tree[node] = _right

    return tree[node]


def update(node, start, end, index, value):
    if index < start or index > end:
        return

    if start == end:
        nums[index] = value
        tree[node] = index
        return

    mid = (start + end) // 2

    update(node * 2, start, mid, index, value)
    update(node * 2 + 1, mid + 1, end, index, value)

    _left = tree[node * 2]
    _right = tree[node * 2 + 1]

    if nums[_left] <= nums[_right]:
        tree[node] = _left
    else:
        tree[node] = _right


def query(node, start, end, left, right):
    if left > end or right < start:
        return -1
    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2

    _left = query(node * 2, start, mid, left, right)
    _right = query(node * 2 + 1, mid + 1, end, left, right)

    if _left == -1:
        return _right

    if _right == -1:
        return _left

    if nums[_left] <= nums[_right]:
        return _left

    return _right


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    tree = [int(1e12) for i in range(4 * n)]
    init(1, 0, n - 1)

    result = list()

    m = int(input())

    for i in range(m):
        q = list(map(int, input().split()))
        if q[0] == 1:
            update(1, 0, n - 1, q[1] - 1, q[2])
        elif q[0] == 2:
            result.append(query(1, 0, n - 1, q[1] - 1, q[2] - 1) + 1)

    print(*result, sep="\n")
