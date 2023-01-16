def toB(n):
    result = list()
    while n > 0:
        result.append(n % 2)
        n = n // 2
    return result[::-1]

def toD(n):
    result = 0
    num = 0
    for digit in n:
        result += int(digit) * (2 ** num)
        num += 1
    return result


n = int(input())
bin = toB(n)
dec = toD(bin)
print(dec)