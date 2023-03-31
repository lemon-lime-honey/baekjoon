t = int(input())

for i in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    max_price = prices[-1]
    total = 0

    for j in range(n - 2, -1, -1):
        if prices[j] > max_price:
            max_price = prices[j]
        else:
            total += max_price - prices[j]
    
    print(f'#{i + 1} {total}')