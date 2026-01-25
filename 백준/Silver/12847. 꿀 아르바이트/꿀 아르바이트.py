n, m = map(int, input().split())
t = list(map(int, input().split()))

result = 0
total = 0
idx = 0
cnt = 0

for i in range(n):
    cnt += 1
    total += t[i]

    if cnt == m:
        result = max(result, total)
        total -= t[idx]
        idx += 1
        cnt -= 1

print(result)
