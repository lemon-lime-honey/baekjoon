import sys

input = sys.stdin.readline


def update(i, diff):
    while i <= n:
        tree[i] += diff
        i += i & -i


def get_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= i & -i
    return result


n = int(input())
a = [0] + list(map(int, input().split()))
b_raw = [0] + list(map(int, input().split()))

b = dict()

for i in range(1, n + 1):
    b[b_raw[i]] = i

tree = [0 for i in range(n + 1)]
result = 0

for i in range(1, n + 1):
    target = b[a[i]]
    result += get_sum(n) - get_sum(target)
    update(target, 1)

print(result)
