n, k, p = map(int, input().split())
cream = list(map(int, input().split()))
result = 0

for i in range(0, n * k, k):
    cnt = 0
    for j in range(i, i + k):
        if cream[j] == 0:
            cnt += 1
    if cnt < p:
        result += 1

print(result)
