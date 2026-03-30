result = list()

while True:
    ipt = input()

    if ipt == "#":
        break

    one = ipt.count("1")

    if one % 2:
        if ipt[-1] == "e":
            result.append(ipt[: len(ipt) - 1] + "1")
        else:
            result.append(ipt[: len(ipt) - 1] + "0")
    else:
        if ipt[-1] == "e":
            result.append(ipt[: len(ipt) - 1] + "0")
        else:
            result.append(ipt[: len(ipt) - 1] + "1")

print(*result, sep="\n")
