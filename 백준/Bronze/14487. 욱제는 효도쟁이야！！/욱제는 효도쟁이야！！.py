n = int(input())
costs = list(map(int, input().split()))
costs.sort()

print(sum(costs) - costs[-1])
