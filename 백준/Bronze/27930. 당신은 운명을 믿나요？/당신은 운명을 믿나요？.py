s = input()
y, k = list(), list()
yy, kk = "YONSEI", "KOREA"
i, j = 0, 0

for letter in s:
    if letter == yy[i]:
        if len(y) == i:
            y.append(letter)
            i += 1
    if letter == kk[j]:
        if len(k) == j:
            k.append(letter)
            j += 1

    if len(y) == 6:
        print("YONSEI")
        break
    if len(k) == 5:
        print("KOREA")
        break