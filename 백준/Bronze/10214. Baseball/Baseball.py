t = int(input())

for i in range(t):
    y, k = 0, 0
    for j in range(9):
        a, b = map(int, input().split())
        y += a
        k += b

    if y > k: print('Yonsei')
    elif y == k: print('Draw')
    else: print('Korea')