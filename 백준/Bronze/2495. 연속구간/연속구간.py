result = 1
cnt = 1

for i in range(3):
    num = input()
    for j in range(7):
        if num[j + 1] == num[j]:
            cnt += 1
            result = max(result, cnt)
        else:
            cnt = 1
    print(result)
    result = 1
    cnt = 1
