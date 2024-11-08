result = 0

for i in range(10):
    ipt = int(input())
    result = (result + ipt) % 4

match result:
    case 0:
        print("N")
    case 1:
        print("E")
    case 2:
        print("S")
    case 3:
        print("W")
