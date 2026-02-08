import sys

sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]

    mid = (start + end) // 2

    left = init(node * 2, start, mid)
    right = init(node * 2 + 1, mid + 1, end)

    tree[node] = min(left, right)

    return tree[node]


def update(node, start, end, index, value):
    if start > index or end < index:
        return
    if start == end:
        tree[node] = value
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, index, value)
    update(node * 2 + 1, mid + 1, end, index, value)

    tree[node] = min(tree[node * 2], tree[node * 2 + 1])


def query(node, start, end, left, right):
    if end < left or start > right:
        return int(1e12)
    if start >= left and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return min(
        query(node * 2, start, mid, left, right),
        query(node * 2 + 1, mid + 1, end, left, right),
    )


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    tree = [int(1e12) for i in range(4 * n + 1)]

    init(1, 0, n - 1)

    m = int(input())
    result = list()

    for i in range(m):
        a, b, c = map(int, input().split())

        if a == 1:
            update(1, 0, n - 1, b - 1, c)
        elif a == 2:
            result.append(query(1, 0, n - 1, b - 1, c - 1))

    print(*result, sep="\n")
