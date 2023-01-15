def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    bef1 = 1
    bef2 = 0
    temp = 0
    for i in range(2, n):
        temp = bef1 + bef2
        bef2 = bef1
        bef1 = temp
    return (bef1 + bef2)

n = int(input())
print(fib(n))