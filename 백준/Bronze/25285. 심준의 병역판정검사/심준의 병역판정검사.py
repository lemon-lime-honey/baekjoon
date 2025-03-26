t = int(input())

for i in range(t):
    height, weight = map(int, input().split())
    if height < 140.1:
        print(6)
    elif height < 146:
        print(5)
    elif height < 159:
        print(4)
    else:
        bmi = weight / (height / 100) ** 2
        if height < 161:
            if 16.0 <= bmi < 35.0:
                print(3)
            else:
                print(4)
        elif height < 204:
            if 20.0 <= bmi < 25.0:
                print(1)
            elif 18.5 <= bmi < 30.0:
                print(2)
            elif 16.0 <= bmi < 35.0:
                print(3)
            else:
                print(4)
        else:
            print(4)
