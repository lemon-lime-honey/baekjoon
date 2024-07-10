h, w, n, m = map(int, input().split())
hor, ver = 0, 0

for i in range(0, w, m + 1):
    hor += 1

for i in range(0, h, n + 1):
    ver += 1

print(hor * ver)