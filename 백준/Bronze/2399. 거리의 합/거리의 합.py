n = int(input())
points = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(n):
        result += abs(points[i] - points[j])

print(result)
