n = int(input())
num = 0

while(1):
    if num == 0:
        n -= 1
    else:
        n -= 6*num
        
    if ((n == 0) or (n < 0)):
        print(num+1)
        break
    num += 1
