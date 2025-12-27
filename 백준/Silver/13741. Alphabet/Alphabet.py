from bisect import bisect_left
import sys

input = sys.stdin.readline

target = input()
result = [target[0]]

for i in range(1, len(target)):
    if result[-1] < target[i]:
        result.append(target[i])
    else:
        idx = bisect_left(result, target[i])
        result[idx] = target[i]

print(26 - len(result))
