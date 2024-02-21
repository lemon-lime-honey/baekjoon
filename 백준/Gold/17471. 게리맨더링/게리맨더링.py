from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline


def calc():
    def bfs(nums):
        for i in range(len(nums)):
            chk = [False for i in range(n + 1)]
            que = deque([nums[0]])
            total = pops[nums[0]]
            chk[nums[0]] = True
            cnt = 1

            while que:
                now = que.popleft()
                for next_point in matrix[now]:
                    if next_point not in nums or chk[next_point]:
                        continue
                    chk[next_point] = True
                    que.append(next_point)
                    total += pops[next_point]
                    cnt += 1

            if cnt == len(nums):
                return total

        return -1


    second = list()

    for i in range(1, n + 1):
        if i not in comb:
            second.append(i)

    one = bfs(comb)
    two = bfs(second)
    if one != -1 and two != -1:
        return abs(one - two)
    return -1


n = int(input())
pops = [0] + list(map(int, input().split()))
matrix = [[] for i in range(n + 1)]
result = int(1e9)

for i in range(1, n + 1):
    ipt = list(map(int, input().split()))
    matrix[i].extend(ipt[1:])

for i in range(1, n // 2 + 1):
    combs = combinations(range(1, n + 1), i)
    for comb in combs:
        res = calc()
        if res != -1:
            result = min(result, res)

print(result if result != int(1e9) else -1)