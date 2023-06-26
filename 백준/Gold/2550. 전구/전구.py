from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
switch = list(map(int, input().split()))
lamp = list(map(int, input().split()))
dp = [1 for i in range(n)]
cable = list()

for i in range(n):
    for j in range(n):
        if switch[i] == lamp[j]:
            cable.append(j)
            break

result = [cable[0]]

for i in range(1, n):
    if result[-1] < cable[i]:
        result.append(cable[i])
        dp[i] = len(result)
    else:
        idx = bisect_left(result, cable[i])
        result[idx] = cable[i]
        dp[i] = idx + 1

ref = len(result)
answer = list()

for i in range(n - 1, -1, -1):
    if ref == 0:
        break
    if dp[i] == ref:
        answer.append(switch[i])
        ref -= 1

print(len(result))
print(*answer[::-1])