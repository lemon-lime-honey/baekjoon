before = int(input())
flat = 0
asc = 0
desc = 0

for i in range(1, 4):
    temp = int(input())
    if (temp == before) * (asc == desc == 0):
        flat = 1
    elif (temp > before) * (flat == desc == 0):
        asc = 1
    elif (temp < before) * (flat == asc == 0):
        desc = 1
    else:
        print('No Fish')
        break
    before = temp
else:
    if flat == 1:
        print('Fish At Constant Depth')
    elif asc == 1:
        print('Fish Rising')
    elif desc == 1:
        print('Fish Diving')