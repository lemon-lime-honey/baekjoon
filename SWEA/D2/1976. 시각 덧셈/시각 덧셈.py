t = int(input())

for i in range(t):
    h1, m1, h2, m2 = map(int, input().split())
    mRes = m1 + m2
    hRes = h1 + h2
    
    if mRes >= 60:
        hRes += mRes // 60
        mRes %= 60
    if hRes > 12:
        hRes %= 12
        if hRes == 0:
            hRes = 12
    
    print(f'#{i + 1} {hRes} {mRes}')