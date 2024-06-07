n = int(input())
result = 0

while n > 9:
    length = len(str(n))
    result += (n - 10 ** (length - 1) + 1) * length
    n = 10 ** (length - 1) - 1

result += n
print(result % 1234567)