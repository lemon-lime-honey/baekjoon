table = {1: 3, 2: 2, 3: 1}

n = list(map(int, input().split()))
dist = list()

for num in n:
    temp = list()
    if num % 4 ==0:
        temp.append(num // 4 - 1)
        temp.append(0)
    else:
        temp.append(num // 4)
        temp.append(table[num % 4])
    dist.append(temp)

print(abs(dist[0][0] - dist[1][0]) + abs(dist[0][1] - dist[1][1]))