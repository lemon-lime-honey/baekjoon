num = list()
maximum = 0
rotation = 0
result = 0

for i in range(2):
    num.append(list(map(int, input().split())))

for i in range(4):
    rotation += 1
    num[0][0], num[0][1] = num[0][1], num[0][0]
    num[0][0], num[1][0] = num[1][0], num[0][0]
    num[1][0], num[1][1] = num[1][1], num[1][0]

    temp = (num[0][0] / num[1][0]) + (num[0][1] / num[1][1])

    if (temp > maximum) or ((temp == maximum) and (rotation % 4 < result)):
        maximum = temp
        result = rotation % 4

print(result)
        