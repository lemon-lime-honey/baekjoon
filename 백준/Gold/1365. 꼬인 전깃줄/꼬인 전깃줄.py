from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
pole = list(map(int, input().split()))
result = [pole[0]]

for i in range(1, n):
    if result[-1] < pole[i]:
        result.append(pole[i])
    else:
        chk = bisect_left(result, pole[i])
        result[chk] = pole[i]

print(n - len(result))