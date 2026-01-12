n = int(input())
names = [input() for i in range(n)]

result = 0

if names[0] > names[1]:
    result = 1

for i in range(2, n):
    if result == 2:
        break
    if names[i - 1] < names[i] and result == 1:
        result = 2
    elif names[i - 1] > names[i] and result == 0:
        result = 2

match result:
    case 0:
        print("INCREASING")
    case 1:
        print("DECREASING")
    case 2:
        print("NEITHER")
