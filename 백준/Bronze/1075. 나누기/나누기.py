n = int(input())
f = int(input())

temp = (n // 100) * 100

for i in range(100):
    if (temp + i) % f == 0:
        if i < 10:
            print('0' + str(i))
        else:
            print(str(i))
        break