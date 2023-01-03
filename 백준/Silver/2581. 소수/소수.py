def chk(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        for i in range(2, num):
            if (num%i)==0:
                return 0
        return 1


m = int(input())
n = int(input())
lst = list()

for i in range(m, n+1):
    if chk(i):
        lst.append(i)

if not lst:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))
