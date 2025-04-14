x = input()

if x[0] != "0":
    print(x)
elif x[1] == "x":
    result = 0
    for i in range(len(x) - 1, 1, -1):
        if x[i].isdigit():
            result += int(x[i]) * (16 ** (len(x) - 1 - i))
        else:
            result += (ord(x[i].lower()) - ord("a") + 10) * (16 ** (len(x) - 1 - i))
    print(result)
else:
    result = 0
    for i in range(len(x) - 1, 0, -1):
        result += int(x[i]) * (8 ** (len(x) - 1 - i))
    print(result)
