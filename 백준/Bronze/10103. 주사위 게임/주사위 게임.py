n = int(input())
c, s = 100, 100

for i in range(n):
    a, b = map(int, input().split())
    if a == b: continue
    if a < b:
        c -= b
    else:
        s -= a

print(c, s, sep='\n')