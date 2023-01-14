a, b = map(int, input().split())
number = [0]

if a == b == 1:
    print(1)
else:
    for i in range(b):
        for j in range(i):
            number.append(i)
    print(sum(number[a:b + 1]))