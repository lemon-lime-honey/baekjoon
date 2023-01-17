l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

cnt = 0

while True:
    a -= c
    b -= d
    cnt += 1
    if (a <= 0) * (b <= 0):
        print(l - cnt)
        break