i1, m1, s1, e1 = map(int, input().split())
i2, m2, s2, e2 = map(int, input().split())

s = sum([i1, m1, s1, e1])
t = sum([i2, m2, s2, e2])

if (s == t):
    print(s)
else:
    print(max(s, t))