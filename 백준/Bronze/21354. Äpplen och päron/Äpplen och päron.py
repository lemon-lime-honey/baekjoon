a, p = map(int, input().split())

axel = a * 7
petra = p * 13

if axel < petra:
    print('Petra')
elif axel == petra:
    print('lika')
else:
    print('Axel')