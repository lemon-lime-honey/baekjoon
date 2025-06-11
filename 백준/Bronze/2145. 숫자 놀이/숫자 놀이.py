while True:
    num = int(input())
    if num == 0:
        break
    while True:
        chk = 0
        while num:
            chk += num % 10
            num //= 10
        if chk < 10:
            print(chk)
            break
        num = chk
