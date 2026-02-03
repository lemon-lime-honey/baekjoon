mirror = {
    "b": "d",
    "d": "b",
    "p": "q",
    "q": "p",
    "i": "i",
    "o": "o",
    "v": "v",
    "w": "w",
    "x": "x",
}

while True:
    ipt = input()

    if ipt == "#":
        break

    result = list()

    for letter in ipt:
        if letter not in mirror:
            print("INVALID")
            break
        result.append(mirror[letter])
    else:
        print("".join(result[::-1]))
