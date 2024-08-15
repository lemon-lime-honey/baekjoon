n, k = map(int, input().split())
ipt = input()

if k == 1: print(ipt)
elif (n - k) % 2:
    print(ipt[k - 1:], ipt[:k - 1], sep='')
else:
    print(ipt[k - 1:], ipt[:k - 1][::-1], sep='')
