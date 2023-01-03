n = int(input())
num = 1

while(1):
    n -= num
    if ((n > 0) != True):
        if (num%2 == 0):
            print('{0}/{1}'.format(num+n, 1-n))
        else:
            print('{0}/{1}'.format(1-n, num+n))
        break

    num+=1
