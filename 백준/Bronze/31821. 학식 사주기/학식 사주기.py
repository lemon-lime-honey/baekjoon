n = int(input())
costs = [int(input()) for i in range(n)]

result = 0

m = int(input())
for i in range(m):
    result += costs[int(input()) - 1]

print(result)
