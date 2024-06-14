data = [int(input()) for i in range(5)]
x = data[4] * data[0]
y = data[1] if data[4] <= data[2] else data[1] + data[3] * (data[4] - data[2])
print(min(x, y))