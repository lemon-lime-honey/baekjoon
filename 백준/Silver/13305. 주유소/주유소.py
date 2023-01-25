n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
total = 0
before = 1000000001

for i in range(n - 1):
    if price[i] < before:
        before = price[i]
    total += before * road[i]

print(total)