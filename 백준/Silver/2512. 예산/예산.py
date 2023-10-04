import sys
input = sys.stdin.readline

n = int(input())
budgets = sorted(list(map(int, input().split())))
total = int(input())
lo, hi = 0, max(budgets)
result = 0

while lo <= hi:
    mid = (lo + hi) // 2
    temp = 0

    for budget in budgets:
        temp += min(budget, mid)

    if total < temp:
        hi = mid - 1
    else:
        lo = mid + 1
        result = mid

print(result)