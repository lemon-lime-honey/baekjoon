t = int(input())

for i in range(t):
    ipt = input().split()
    result = float(ipt[0])

    for j in range(1, len(ipt)):
        if ipt[j] == '@':
            result *= 3
        elif ipt[j] == '%':
            result += 5
        elif ipt[j] == '#':
            result -= 7
   
    print(f'{result:.2f}')