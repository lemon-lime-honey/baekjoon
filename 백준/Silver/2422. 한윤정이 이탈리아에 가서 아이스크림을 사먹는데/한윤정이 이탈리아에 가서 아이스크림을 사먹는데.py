from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dont = defaultdict(set)
result = 0

for i in range(m):
    a, b = map(int, input().split())
    dont[a].add(b)
    dont[b].add(a)

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if j not in dont[i]:
            for k in range(j + 1, n + 1):
                if k not in dont[i] and k not in dont[j]:
                    result += 1

print(result)