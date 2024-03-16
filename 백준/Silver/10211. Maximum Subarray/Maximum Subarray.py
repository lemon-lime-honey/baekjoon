import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    prefix = [0 for i in range(n)]
    prefix[0] = x[0]
    result = -int(1e6)

    for j in range(1, n):
        prefix[j] = prefix[j - 1] + x[j]

    for j in range(n):
        for k in range(j, n):
            result = max(result, prefix[k] - prefix[j] + x[j])

    print(result)