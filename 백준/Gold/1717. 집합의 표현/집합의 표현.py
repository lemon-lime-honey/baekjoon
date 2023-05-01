import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))


def find(num):
    if numbers[num] != num:
        numbers[num] = find(numbers[num])
    return numbers[num]


def union(n1, n2):
    n1, n2 = find(n1), find(n2)

    if n1 == n2: return
    elif n1 < n2: numbers[n2] = n1
    else: numbers[n1] = n2


n, m = map(int, input().split())
numbers = [i for i in range(n + 1)]

for i in range(m):
    ipt = list(map(int, input().split()))

    if ipt[0] == 0:
        union(ipt[1], ipt[2])
    else:
        print('YES' if find(ipt[1]) == find(ipt[2]) else 'NO')