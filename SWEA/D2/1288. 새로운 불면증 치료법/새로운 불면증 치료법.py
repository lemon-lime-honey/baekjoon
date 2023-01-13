T = int(input())

def chk(num, cnt):
    while num > 0:
        cnt[num % 10] += 1
        num = num // 10

for i in range(T):
    cnt = [0] * 10
    num = int(input())
    n = 1
    while True:
        temp = num * n
        chk(temp, cnt)
        if 0 not in cnt:
            break
        n += 1
    print(f'#{i + 1} {n * num}')