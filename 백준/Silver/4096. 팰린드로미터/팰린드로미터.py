def palindrome(n):
    num = int(n)
    length = len(n)
    ref = num
    result = 0
    while True:
        if str(ref).zfill(length) == str(ref)[::-1].ljust(length, '0'):
            return result
        result += 1
        ref += 1

while True:
    n = input()
    if n == '0':
        break
    print(palindrome(n))