d, h, m = map(int, input().split())

if (d == 11) * ((h == 11) * (m < 11) + (h < 11)):
    print(-1)
else:
    resD = d - 11
    if h < 11:
        resD -= 1
        resH = 24 + h - 11
    else:
        resH = h - 11
    if m < 11:
        resH -= 1
        resM = 60 + m - 11
    else:
        resM = m - 11
    print(resD * 24 * 60 + resH * 60 + resM)