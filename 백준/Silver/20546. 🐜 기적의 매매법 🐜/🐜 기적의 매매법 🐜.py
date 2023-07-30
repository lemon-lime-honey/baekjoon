money = int(input())
s, j = money, money
costs = list(map(int, input().split()))
jh, sm = 0, 0

for i in range(14):
    if j >= costs[i]:
        jh += j // costs[i]
        j %= costs[i]
    if i > 2:
        if (
            costs[i - 3] < costs[i - 2] and 
            costs[i - 2] < costs[i - 1] and 
            costs[i - 1] < costs[i]
        ):
            s += sm * costs[i]
            sm = 0
        elif (
            costs[i - 3] > costs[i - 2] and 
            costs[i - 2] > costs[i - 1] and 
            costs[i - 1] > costs[i]
        ):
            if s >= costs[i]:
                sm += s // costs[i]
                s %= costs[i]

if (j + costs[-1] * jh) > (s + costs[-1] * sm):
    print('BNP')
elif (j + costs[-1] * jh) < (s + costs[-1] * sm):
    print('TIMING')
else:
    print('SAMESAME')