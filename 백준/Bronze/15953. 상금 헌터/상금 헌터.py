t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    result = 0
    if a != 0:
        if a < 2:
            result += 5000000
        elif a < 4:
            result += 3000000
        elif a < 7:
            result += 2000000
        elif a < 11:
            result += 500000
        elif a < 16:
            result += 300000
        elif a < 22:
            result += 100000
    if b != 0:
        if b < 2:
            result += 5120000
        elif b < 4:
            result += 2560000
        elif b < 8:
            result += 1280000
        elif b < 16:
            result += 640000
        elif b < 32:
            result += 320000
    print(result)