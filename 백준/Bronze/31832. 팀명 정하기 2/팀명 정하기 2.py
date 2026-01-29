n = int(input())
names = [input() for i in range(n)]

for target in names:
    if len(target) > 10:
        continue

    size = [0, 0]
    flag = False

    for letter in target:
        if not letter.isdigit():
            flag = True
        if letter.isalpha():
            if letter.isupper():
                size[0] += 1
            else:
                size[1] += 1

    if not flag:
        continue

    if size[0] <= size[1]:
        print(target)
        break
