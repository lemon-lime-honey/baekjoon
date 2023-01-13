t = int(input())

for i in range(t):
    p, q, r, s, w = map(int, input().split())
    a = p * w
    if w <= r:
        b = q
    else:
        b = q + (w - r) * s
    if a < b:
        print(f'#{i + 1} {a}')
    else:
        print(f'#{i + 1} {b}')