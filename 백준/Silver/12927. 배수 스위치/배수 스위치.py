ipt = input()
light = [False for i in range(len(ipt) + 1)]
result = 0

for i in range(len(ipt)):
    if ipt[i] == 'Y':
        light[i + 1] = True

while True:
    for i in range(1, len(ipt) + 1):
        if light[i]:
            break
    else:
        break

    for i in range(1, len(ipt) + 1):
        if light[i]:
            result += 1
            for j in range(i, len(ipt) + 1, i):
                light[j] = not light[j]

print(result)
