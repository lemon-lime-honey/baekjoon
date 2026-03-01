import sys

sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline


def init_even(node, start, end):
    if start == end:
        even[node] = 0 if nums[start] % 2 else 1
        return even[node]

    mid = (start + end) // 2
    _left = init_even(node * 2, start, mid)
    _right = init_even(node * 2 + 1, mid + 1, end)

    even[node] = _left + _right

    return even[node]


def init_odd(node, start, end):
    if start == end:
        odd[node] = 1 if nums[start] % 2 else 0
        return odd[node]

    mid = (start + end) // 2
    _left = init_odd(node * 2, start, mid)
    _right = init_odd(node * 2 + 1, mid + 1, end)

    odd[node] = _left + _right

    return odd[node]


def update_even(node, start, end, index, value):
    if index < start or index > end:
        return

    if start == end:
        even[node] = 0 if value % 2 else 1
        return

    mid = (start + end) // 2
    update_even(node * 2, start, mid, index, value)
    update_even(node * 2 + 1, mid + 1, end, index, value)

    even[node] = even[node * 2] + even[node * 2 + 1]


def update_odd(node, start, end, index, value):
    if index < start or index > end:
        return

    if start == end:
        odd[node] = 1 if value % 2 else 0
        return

    mid = (start + end) // 2
    update_odd(node * 2, start, mid, index, value)
    update_odd(node * 2 + 1, mid + 1, end, index, value)

    odd[node] = odd[node * 2] + odd[node * 2 + 1]


def query(node, start, end, left, right, tree):
    if right < start or end < left:
        return 0

    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2
    _left = query(node * 2, start, mid, left, right, tree)
    _right = query(node * 2 + 1, mid + 1, end, left, right, tree)

    return _left + _right


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    even = [0 for i in range(4 * n + 1)]
    odd = [0 for i in range(4 * n + 1)]
    result = list()

    m = int(input())

    init_even(1, 0, n - 1)
    init_odd(1, 0, n - 1)

    for i in range(m):
        a, b, c = map(int, input().split())

        if a == 1:
            update_even(1, 0, n - 1, b - 1, c)
            update_odd(1, 0, n - 1, b - 1, c)
        elif a == 2:
            result.append(query(1, 0, n - 1, b - 1, c - 1, even))
        else:
            result.append(query(1, 0, n - 1, b - 1, c - 1, odd))

    print(*result, sep="\n")
