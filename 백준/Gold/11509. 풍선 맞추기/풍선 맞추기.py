n = int(input())
h = list(map(int, input().split()))

arrow = [0 for i in range(int(1e6) + 1)]
result = 0

for height in h:
    if arrow[height] == 0:
        result += 1
        arrow[height - 1] += 1
    else:
        arrow[height] -= 1
        arrow[height - 1] += 1

print(result)