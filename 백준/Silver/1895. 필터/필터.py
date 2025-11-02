r, c = map(int, input().split())

image = [list(map(int, input().split())) for i in range(r)]
result = list()

t = int(input())

for i in range(r - 2):
    for j in range(c - 2):
        targets = list()
        for k in range(3):
            for l in range(3):
                targets.append(image[i + k][j + l])
        targets.sort()
        result.append(targets[4])

result.sort()

for i in range(len(result)):
    if t <= result[i]:
        print(len(result) - i)
        break
else:
    print(0)
