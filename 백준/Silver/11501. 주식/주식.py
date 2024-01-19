import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    costs = list(map(int, input().split()))
    high = costs[-1]
    result = 0

    for j in range(n - 2, -1, -1):
        if costs[j] < high:
            result += high - costs[j]
        elif costs[j] > high:
            high = costs[j]

    print(result)