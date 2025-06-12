from collections import Counter
import sys
input = sys.stdin.readline

t = int(input())
result = list()

for i in range(t):
    n = int(input())
    candy = list(map(int, input().split()))
    cnt = 0

    for i in range(n):
        if candy[i] % 2:
            candy[i] += 1

    while len(Counter(candy)) != 1:
        temp = [0 for i in range(n)]
        for i in range(n):
            if i < n - 1:
                temp[i + 1] = candy[i] // 2
            else:
                temp[0] = candy[i] // 2
            candy[i] //= 2
        for i in range(n):
            candy[i] += temp[i]
        for i in range(n):
            if candy[i] % 2:
                candy[i] += 1
        cnt += 1

    result.append(cnt)

print(*result, sep="\n")
