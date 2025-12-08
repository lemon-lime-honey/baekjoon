a, b, c = map(int, input().split())
n = int(input())
result = 0

for i in range(n):
    score = 0
    for j in range(3):
        u, v, w = map(int, input().split())
        score += u * a + v * b + w * c
    result = max(result, score)

print(result)
