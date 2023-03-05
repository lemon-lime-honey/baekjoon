from collections import Counter
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a_cnt = Counter(a)
result = [-1] * n
stack = list()

for idx, num in enumerate(a):
    while stack:
        if a_cnt[stack[-1][0]] < a_cnt[num]:
            result[stack[-1][1]] = num
            stack.pop()
        else:
            break
    stack.append((num, idx))

print(*result)