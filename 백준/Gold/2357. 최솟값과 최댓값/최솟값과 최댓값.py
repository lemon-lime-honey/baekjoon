def max_init(node, start, end):
    if start == end:
        maximum[node] = nums[start]
        return maximum[node]
    mid = (start + end) // 2
    maximum[node] = max(
        max_init(node * 2, start, mid), max_init(node * 2 + 1, mid + 1, end)
    )
    return maximum[node]


def min_init(node, start, end):
    if start == end:
        minimum[node] = nums[start]
        return minimum[node]
    mid = (start + end) // 2
    minimum[node] = min(
        min_init(node * 2, start, mid), min_init(node * 2 + 1, mid + 1, end)
    )
    return minimum[node]


def min_query(node, start, end, left, right):
    if left > end or right < start:
        return int(1e12)
    if left <= start and right >= end:
        return minimum[node]
    mid = (start + end) // 2
    return min(
        min_query(node * 2, start, mid, left, right),
        min_query(node * 2 + 1, mid + 1, end, left, right),
    )


def max_query(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return maximum[node]
    mid = (start + end) // 2
    return max(
        max_query(node * 2, start, mid, left, right),
        max_query(node * 2 + 1, mid + 1, end, left, right),
    )


if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = [int(input()) for i in range(n)]
    minimum = [int(1e12) for i in range(4 * n)]
    maximum = [0 for i in range(4 * n)]

    result = list()

    min_init(1, 0, n - 1)
    max_init(1, 0, n - 1)

    for i in range(m):
        a, b = map(int, input().split())
        result.append(
            (min_query(1, 0, n - 1, a - 1, b - 1), max_query(1, 0, n - 1, a - 1, b - 1))
        )

    for a, b in result:
        print(a, b)
