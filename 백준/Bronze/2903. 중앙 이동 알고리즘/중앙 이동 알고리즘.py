number = [0 for i in range(15)]
number[0] = 3

for i in range(1, 15):
    number[i] = 2 * number[i - 1] - 1

n = int(input())
print(number[n - 1] ** 2)