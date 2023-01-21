t1, m1, t2, m2 = map(int, input().split())

if (t1 == t2) * (m2 < m1):
    h = 23
    m = 60 + m2 - m1
else:
    if t2 < t1:
        t2 += 24
    h = t2 - t1

    if m2 < m1:
        h -= 1
        m2 += 60
    m = m2 - m1
total = h * 60 + m

print(f'{total} {total // 30}')