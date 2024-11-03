n = int(input())
num = 10

while n > num:
    if n % num >= num // 2:
        n += num
    n -= n % num
    num *= 10

print(n)
