tile = [0, 1, 2]

for i in range(1000000):
    tile.append((tile[-1] + tile[-2]) % 15746)

n = int(input())
print(tile[n])