number = [0, 1, 2, 4, 7, 0, 0, 0, 0, 0, 0]

for i in range(5, 11):
    number[i] = number[i - 1] + number[i - 2] + number[i - 3]

t = int(input())

for i in range(t):
    n = int(input())
    print(number[n])