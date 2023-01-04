t = int(input())
a = b = c = 0
flag = 0

while True:
    if t >= 300:
        t -= 300
        a += 1
    elif t >= 60:
        t -= 60
        b += 1
    elif t >= 10:
        t -= 10
        c += 1
    elif t == 0:
        break
    else:
        flag = 1
        break

if flag:
    print(-1)
else:
    print(f'{a} {b} {c}')