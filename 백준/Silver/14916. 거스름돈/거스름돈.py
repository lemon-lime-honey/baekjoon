coin = [0, 10 ** 6, 1, 10 ** 6, 2, 1]
for i in range(10 ** 5):
    coin.append(min(coin[-2] + 1, coin[-5] + 1))

n = int(input())
if coin[n] == 10 ** 6:
    print(-1)
else:
    print(coin[n])