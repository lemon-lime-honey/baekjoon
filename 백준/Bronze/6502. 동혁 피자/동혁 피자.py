idx = 1

while True:
    ipt = list(map(int, input().split()))
    if ipt[0] == 0:
        break
    length = ipt[1] ** 2 + ipt[2] ** 2
    if (ipt[0] * 2) ** 2 >= length:
        print(f"Pizza {idx} fits on the table.")
    else:
        print(f"Pizza {idx} does not fit on the table.")
    idx += 1
