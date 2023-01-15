n = int(input())

while True:
    if (str(n)[::-1] != str(n)) + (n == 1):
        n += 1
        continue
    else:
        for i in range(2, n):
            if n % i == 0:
                n += 1
                break
        else:
            print(n)
            break