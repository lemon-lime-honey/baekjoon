import sys

sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)

    return tree[node]


def update(node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = val
        return

    mid = (start + end) // 2

    update(node * 2, start, mid, index, val)
    update(node * 2 + 1, mid + 1, end, index, val)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]

    return


def query(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2

    left_sum = query(node * 2, start, mid, left, right)
    right_sum = query(node * 2 + 1, mid + 1, end, left, right)

    return left_sum + right_sum


n, m, k = map(int, input().split())

nums = [int(input()) for i in range(n)]
tree = [0 for i in range(4 * n)]

init(1, 0, n - 1)

for i in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        update(1, 0, n - 1, b - 1, c)
    else:
        result = query(1, 0, n - 1, b - 1, c - 1)
        print(result)
