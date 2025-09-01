from collections import Counter

n = int(input())
result = 0

for i in range(n):
    dice = list(map(int, input().split()))
    cnt = sorted(Counter(dice).items(), key=lambda x: (-x[1], -x[0]))

    if cnt[0][1] == 4:
        result = max(result, 50000 + cnt[0][0] * 5000)
    elif cnt[0][1] == 3:
        result = max(result, 10000 + cnt[0][0] * 1000)
    elif cnt[0][1] == 2 and cnt[1][1] == 2:
        result = max(result, 2000 + (cnt[0][0] + cnt[1][0]) * 500)
    elif cnt[0][1] == 2:
        result = max(result, 1000 + cnt[0][0] * 100)
    else:
        result = max(result, cnt[0][0] * 100)

print(result)
