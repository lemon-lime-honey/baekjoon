from collections import deque

n, m, l = map(int, input().split())

cnt = deque([0 for i in range(n)])
cnt[0] = 1
result = 0

while True:
    if m in cnt:
        break
    result += 1
    if cnt[0] % 2:
        cnt.rotate(l)
        cnt[0] += 1
    else:
        cnt.rotate(-l)
        cnt[0] += 1

print(result)
