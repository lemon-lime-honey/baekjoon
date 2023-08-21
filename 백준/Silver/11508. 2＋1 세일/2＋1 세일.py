import sys
input = sys.stdin.readline

n = int(input())
dairy = sorted([int(input()) for i in range(n)], reverse=True)
dairy_sets = list()
result = 0

for i in range(0, n, 3):
    dairy_sets.append(dairy[i:i+3])

for costs in dairy_sets:
    if len(costs) > 2:
        result += sum(costs) - min(costs)
    else:
        result += sum(costs)

print(result)