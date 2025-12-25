n = int(input())
box = list(map(int, input().split()))
result = [1 for i in range(n)]

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if box[i] < box[j]:
            result[i] = max(result[i], result[j] + 1)

print(max(result))
