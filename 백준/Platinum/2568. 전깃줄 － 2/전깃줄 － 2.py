from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
cables = list()
answer = set()

for i in range(n):
    ipt = tuple(map(int, input().split()))
    cables.append(ipt)
    answer.add(ipt[0])

dp = [1 for i in range(n)]
result = list()
cables.sort()

for i in range(n):
    start, end = cables[i]
    if not result:
        result.append(end)
    else:
        if result[-1] < end:
            result.append(end)
            dp[i] = len(result)
        else:
            chk = bisect_left(result, end)
            result[chk] = end
            dp[i] = chk + 1

ref = len(result)
print(n - ref)

for i in range(n - 1, -1, -1):
    if dp[i] == ref:
        answer.remove(cables[i][0])
        ref -= 1

answer = sorted(answer)
print(*answer, sep='\n')