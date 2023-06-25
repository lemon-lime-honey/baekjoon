from bisect import bisect_left
import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        cost = list(map(int, input().split()))
        result = [cost[0]]
        for i in range(1, n):
            if result[-1] < cost[i]:
                result.append(cost[i])
            else:
                idx = bisect_left(result, cost[i])
                result[idx] = cost[i]
        print(len(result))
    except:
        break