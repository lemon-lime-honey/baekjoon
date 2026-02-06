import sys

sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = min(init(node * 2, start, mid), init(node * 2 + 1, mid + 1, end))
    return tree[node]


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
    n, m = map(int, input().split())

    nums = [int(input()) for i in range(n)]
    tree = [int(1e12) for i in range(4 * n)]
    result = list()

    init(1, 0, n - 1)

    for i in range(m):
        a, b = map(int, input().split())
        result.append(query(1, 0, n - 1, a - 1, b - 1))

    print(*result, sep="\n")
