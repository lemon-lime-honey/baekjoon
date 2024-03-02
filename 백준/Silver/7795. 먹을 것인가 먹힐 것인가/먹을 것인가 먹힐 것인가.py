from bisect import bisect_right
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))
    result = 0

    for creature in a:
        idx = bisect_right(b, creature)
        result += idx
        while idx > 0 and creature == b[idx - 1]:
            result -= 1
            idx -= 1

    print(result)