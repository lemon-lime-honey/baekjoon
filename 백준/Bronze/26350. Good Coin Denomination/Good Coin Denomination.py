n = int(input())

for i in range(n):
    data = list(map(int, input().split()))
    coin = list(map(int, data[1:]))
    before = coin[0]
    
    print('Denominations:', end = ' ')
    print(*coin)
    
    for j in range(1, data[0]):
        if coin[j] < 2 * before:
            print('Bad coin denominations!')
            break
        else:
            before = coin[j]
    else:
        print('Good coin denominations!')
    
    print()