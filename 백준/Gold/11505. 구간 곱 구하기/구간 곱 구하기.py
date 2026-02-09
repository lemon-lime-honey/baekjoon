import sys

sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]

    mid = (start + end) // 2

    init(node * 2, start, mid)
    init(node * 2 + 1, mid + 1, end)

    tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % 1000000007

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

    tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % 1000000007

    return


def query(node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2

    left_mul = query(node * 2, start, mid, left, right)
    right_mul = query(node * 2 + 1, mid + 1, end, left, right)

    return (left_mul * right_mul) % 1000000007


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    nums = [int(input()) for i in range(n)]
    tree = [1 for i in range(4 * n)]
    result = list()

    init(1, 0, n - 1)

    for i in range(m + k):
        a, b, c = map(int, input().split())

        if a == 1:
            update(1, 0, n - 1, b - 1, c)
        elif a == 2:
            result.append(query(1, 0, n - 1, b - 1, c - 1))

    print(*result, sep="\n")
