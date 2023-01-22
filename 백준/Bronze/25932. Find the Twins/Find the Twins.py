n = int(input())

for i in range(n):
    ipt = input()
    people = list(map(int, ipt.split()))
    mack = False
    zack = False
    
    for num in people:
        if num == 18:
            mack = True
        elif num == 17:
            zack = True
    
    print(ipt)
    
    if mack * zack:
        print('both')
    elif mack:
        print('mack')
    elif zack:
        print('zack')
    else:
        print('none')
    
    print()