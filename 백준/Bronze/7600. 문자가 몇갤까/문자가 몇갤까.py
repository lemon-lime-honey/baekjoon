result = list()

while True:
    ipt = input()

    if ipt == "#":
        break

    alpha = set()

    for letter in ipt.lower():
        if letter.isalpha():
            alpha.add(letter)

    result.append(len(alpha))

print(*result, sep="\n")
