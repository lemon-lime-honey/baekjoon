while True:
    ipt = input()
    if ipt[0] == "#":
        break
    result = 0
    for letter in ipt[2:]:
        if letter.lower() == ipt[0]:
            result += 1
    print(f"{ipt[0]} {result}")
