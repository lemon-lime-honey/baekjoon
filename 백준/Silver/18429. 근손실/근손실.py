import sys
input = sys.stdin.readline


def solve(cnt, weight):
    if cnt == n:
        if weight >= 500:
            global result
            result += 1
        return
    for i in range(n):
        if i in used or weight - k + a[i] < 500: continue
        used.add(i)
        solve(cnt + 1, weight - k + a[i])
        used.discard(i)


n, k = map(int, input().split())
a = list(map(int, input().split()))
used = set()
result = 0
solve(0, 500)
print(result)
