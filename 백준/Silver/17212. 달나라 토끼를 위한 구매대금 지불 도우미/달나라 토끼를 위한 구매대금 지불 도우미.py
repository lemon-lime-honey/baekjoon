n = int(input())
coins = [0, 1, 1, 2, 2, 1, 2, 1]

for i in range(8, n + 1):
    coins.append(min(coins[i - 1], coins[i - 2], coins[i - 5], coins[i - 7]) + 1)

print(coins[n])