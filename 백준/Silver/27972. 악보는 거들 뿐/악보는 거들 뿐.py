m = int(input())
p = list(map(int, input().split()))
ud, cnt, result = 1, 1, 1

for i in range(1, m):
    if p[i] < p[i - 1]:
        if ud:
            ud = 0
            cnt = 2
        else:
            cnt += 1
    elif p[i - 1] < p[i]:
        if ud:
            cnt += 1
        else:
            ud = 1
            cnt = 2
    else: continue
    result = max(result, cnt)

print(result)
