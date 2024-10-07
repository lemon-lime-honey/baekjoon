a, b = input().split()
ta, tb = -1, -1

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            ta, tb = i, j
            break
    if ta != -1 and tb != -1:
        break

for i in range(len(b)):
    if i == tb:
        print(a)
        continue
    for j in range(len(a)):
        if j == ta:
            print(b[i], end='')
        else:
            print('.', end='')
    print()