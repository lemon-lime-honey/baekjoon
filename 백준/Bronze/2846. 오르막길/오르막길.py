n = int(input())
road = list(map(int, input().split()))
maximum = 0
total = 0

for i in range(1, n):
    if road[i] > road[i - 1]:
        total += road[i] - road[i - 1]
    else:
        if total > maximum:
            maximum = total
        total = 0

if total > maximum:
            maximum = total

print(maximum)