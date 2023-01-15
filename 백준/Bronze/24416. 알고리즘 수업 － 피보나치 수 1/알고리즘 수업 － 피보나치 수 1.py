def fibRec(n, cnt):
    if (n == 1) + (n == 2):
        cnt[0] += 1
        return 1
    else:
        return (fibRec(n - 1, cnt) + fibRec(n - 2, cnt))

def fibDP(n, cnt):
    if (n == 1) + (n == 2):
        cnt[1] += 1
        return 1
    else:
        bef1 = 1
        bef2 = 1
        temp = 0
        for i in range(2, n):
            cnt[1] += 1
            temp = bef1 + bef2
            bef2 = bef1
            bef1 = temp
        return (bef1 + bef2)

n = int(input())
cnt = [0, 0]
fibRec(n, cnt)
fibDP(n, cnt)

print(f'{cnt[0]} {cnt[1]}')