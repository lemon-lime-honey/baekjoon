from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
books = list(map(int, input().split()))
result = [books[0]]

for i in range(1, n):
    if result[-1] < books[i]:
        result.append(books[i])
    else:
        idx = bisect_left(result, books[i])
        result[idx] = books[i]

print(n - len(result))