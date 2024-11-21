import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    result = list()

    while prices:
        price = prices.pop()
        target = price * 3 // 4
        if target in prices:
            result.append(target)
            prices.remove(target)

    print(f"Case #{i + 1}:", *sorted(result))
