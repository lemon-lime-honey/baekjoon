def isPrime(num):
    if num < 2: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: return False
    return True


def getNum(num, length):
    if length == 0: print(num)
    for i in range(1, 10, 2):
        temp = num * 10 + i
        if isPrime(temp):
            getNum(temp, length - 1)


n = int(input())

for i in (2, 3, 5, 7):
    getNum(i, n - 1)