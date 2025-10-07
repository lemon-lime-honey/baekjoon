n, k = map(int, input().split())
track = list(map(int, input().split()))

result = 0

for i in range(1, n):
    if track[i - 1] < track[i]:
        continue
    if track[i - 1] < track[i] + k:
        track[i] += k
        result += 1
        continue
    print(-1)
    break
else:
    print(result)
