t = int(input())

for i in range(t):
    num = input()
    result = 0

    while num != '6174':
        result += 1
        num = str(int(''.join(sorted(num, reverse=True))) - int(''.join(sorted(num))))
        if len(num) < 4:
            for j in range(4 - len(num)):
                num += '0'

    print(result)
