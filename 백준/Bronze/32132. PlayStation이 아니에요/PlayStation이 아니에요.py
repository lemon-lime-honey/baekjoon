n = int(input())
target = input()
result = list()

for letter in target:
    if letter not in "45":
        result.append(letter)
    else:
        if len(result) < 2:
            result.append(letter)
        else:
            if result[-1] == "S" and result[-2] == "P":
                continue
            result.append(letter)

print("".join(result))
