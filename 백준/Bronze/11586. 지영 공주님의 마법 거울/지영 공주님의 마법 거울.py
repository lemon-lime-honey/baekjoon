n = int(input())
shape = [input() for i in range(n)]
state = int(input())

match state:
    case 1:
        print(*shape, sep="\n")
    case 2:
        for i in range(n):
            print(shape[i][::-1])
    case 3:
        for i in range(n - 1, -1, -1):
            print(shape[i])
