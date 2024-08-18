from collections import deque
import sys

input = sys.stdin.readline


def dfs(num, start):
    if chk[num]:
        if num == start:
            global flag
            flag = True
            result.add(start)
        return
    chk[num] = True
    dfs(nums[num], start)
    if flag:
        result.add(num)
        result.add(nums[num])


n = int(input())
nums = [0]
for i in range(n):
    nums.append(int(input()))

result = set()

for i in range(1, n + 1):
    chk = [False for i in range(n + 1)]
    flag = False
    dfs(i, i)


print(len(result), *sorted(result), sep='\n')
