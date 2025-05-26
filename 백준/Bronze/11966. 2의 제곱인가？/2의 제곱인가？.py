n = int(input())
table = [2 ** i for i in range(31)]

if n in table:
    print(1)
else:
    print(0)
