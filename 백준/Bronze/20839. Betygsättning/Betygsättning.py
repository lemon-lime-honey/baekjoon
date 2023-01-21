ref = list(map(int, input().split()))
student = list(map(int, input().split()))

if student[1] * 2 < ref[1]:
    print('E')
elif student[1] != ref[1]:
    print('D')
elif student[0] * 2 < ref[0]:
    print('C')
elif student[0] != ref[0]:
    print('B')
else:
    print('A')