n = int(input())
num = n
temp = 0
cycle = 0

while(1):
    if (num<10):
        num *= 11
    else:
        temp = num//10 + num%10
        num = (num%10)*10 + temp%10
    if num == n:
        cycle += 1
        break
    cycle += 1

print(cycle)
