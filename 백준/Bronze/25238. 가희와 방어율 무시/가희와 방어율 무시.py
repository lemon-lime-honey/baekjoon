num = list(map(int, input().split()))
if (num[0] * ((100 - num[1]) / 100) <100):
    print(1)
else:
    print(0)