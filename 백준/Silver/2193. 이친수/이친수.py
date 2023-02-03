number = [0, 1]
for i in range(2, 91):
    number.append(number[i - 1] + number[i - 2])

n = int(input())
print(number[n])