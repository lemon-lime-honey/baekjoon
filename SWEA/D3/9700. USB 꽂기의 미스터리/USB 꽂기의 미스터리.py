tc = int(input())

for i in range(tc):
    p, q = map(float, input().split())
    s1 = (1 - p) * q
    s2 = p * (1 - q) * q
    if s1 < s2:
        print(f'#{i + 1} YES')
    else:
        print(f'#{i + 1} NO')