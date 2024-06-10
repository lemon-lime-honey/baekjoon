from bisect import bisect_left
import sys
input = sys.stdin.readline


def get(n, k, costs):
    result = [costs[0]]

    for i in range(1, n):
        if result[-1] < costs[i]:
            result.append(costs[i])
        else:
            idx = bisect_left(result, costs[i])
            result[idx] = costs[i]

    return 1 if k <= len(result) else 0


t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    costs = list(map(int, input().split()))
    print(f'Case #{i + 1}')
    print(get(n, k, costs))