n = int(input())

for i in range(n):
    ipt = input()
    stats = list(map(int, ipt.split()))
    ten = 0
    
    for stat in stats:
        if stat >= 10:
            ten += 1
    
    print(ipt)
    
    if ten == 0:
        print('zilch')
    elif ten == 1:
        print('double')
    elif ten == 2:
        print('double-double')
    else:
        print('triple-double')
    
    print()