n, x = map(int, input().split())
costs = list(map(int, input().split()))
result = int(1e9)

for i in range(n - 1):
    result = min(result, costs[i] + costs[i + 1])

print(result * x)