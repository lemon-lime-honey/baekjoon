def div(num):
    for i in range(2, num+1):
        if (num%i)==0:
            return i

n = int(input())
divRes = 0

if n!=1:
    while(1):
        divRes = div(n)
        if divRes == n:
            print(n)
            break
        else:
            print(divRes)
            n = n//divRes
