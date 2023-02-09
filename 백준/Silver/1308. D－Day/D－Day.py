import datetime

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

today = datetime.date(y1, m1, d1)
d_day = datetime.date(y2, m2, d2)

if ((y2 - y1 == 1000) and ((m2 > m1) or (m1 == m2 and d2 >= d1))) or (y2 - y1 > 1000):
    print('gg')
else:
    print(f'D-{(d_day - today).days}')