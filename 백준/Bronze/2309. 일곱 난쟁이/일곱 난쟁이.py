height = list()

for i in range(9):
    height.append(int(input()))

height.sort()
total = sum(height)
flag = False

for i in range(9):
    for j in range(9):
        if i != j:
            if total - (height[i] + height[j]) == 100:
                flag = True
                break
    if flag:
        break

for k in range(9):
    if k not in (i, j):
        print(height[k])