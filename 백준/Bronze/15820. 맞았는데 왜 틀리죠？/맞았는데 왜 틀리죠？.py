one, two = map(int, input().split())
flag = -1

for i in range(one):
    a, b = map(int, input().split())
    if a != b:
        flag = 0

for j in range(two):
    a, b = map(int, input().split())
    if a != b:
        if flag == -1:
            flag = 1

match flag:
    case -1:
        print("Accepted")
    case 0:
        print("Wrong Answer")
    case 1:
        print("Why Wrong!!!")