n, k, l = map(int, input().split())
result = list()

for i in range(n):
    score = list(map(int, input().split()))
    if min(score) < l:
        continue
    if sum(score) < k:
        continue
    result.extend(score)

print(len(result) // 3)
print(*result)
