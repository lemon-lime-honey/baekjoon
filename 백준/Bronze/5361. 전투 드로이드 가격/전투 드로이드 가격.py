t = int(input())
costs = [350.34, 230.90, 190.55, 125.30, 180.90]

for i in range(t):
    nums = list(map(int, input().split()))
    result = 0
    for j in range(5):
        result += costs[j] * nums[j]
    print(f"${result:.2f}")
