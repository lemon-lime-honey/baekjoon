def three(n):
    result = 0
    cnt = 0
    while True:
        if int(n) < 10:
            result = int(n)
        else:
            for digit in n:
                result += int(digit)
            cnt += 1
        if result < 10:
            if result % 3 == 0:
                return ([cnt, 'YES'])
            else:
                return ([cnt, 'NO'])
        n = str(result)
        result = 0

x = input()
result = three(x)
print(f'{result[0]}\n{result[1]}')