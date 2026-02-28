import sys

sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = 1 if nums[start] > 0 else -1 if nums[start] < 0 else 0
        return tree[node]

    mid = (start + end) // 2
    _left = init(node * 2, start, mid)
    _right = init(node * 2 + 1, mid + 1, end)

    tree[node] = _left * _right

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

    tree[node] = tree[node * 2] * tree[node * 2 + 1]


def query(node, start, end, left, right):
    if right < start or end < left:
        return 1

    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2
    _left = query(node * 2, start, mid, left, right)
    _right = query(node * 2 + 1, mid + 1, end, left, right)

    return _left * _right


if __name__ == "__main__":
    result = list()

    while True:
        try:
            n, k = map(int, input().split())
            nums = list(map(int, input().split()))
            tree = [1 for i in range(4 * n + 1)]
            res = list()

            init(1, 0, n - 1)

            for i in range(k):
                command = input().split()
                a, b = int(command[1]), int(command[2])

                if command[0] == "C":
                    update(1, 0, n - 1, a - 1, 1 if b > 0 else -1 if b < 0 else 0)
                else:
                    answer = query(1, 0, n - 1, a - 1, b - 1)
                    if answer < 0:
                        res.append("-")
                    elif answer > 0:
                        res.append("+")
                    else:
                        res.append("0")

            result.append("".join(res))
        except Exception:
            break

    print(*result, sep="\n")
