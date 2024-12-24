fmt = input()
idx = 0
result = 1

for i in range(len(fmt)):
    if i == 0:
        if fmt[i] == "c":
            result *= 26
        else:
            result *= 10
        continue
    if fmt[i] == fmt[i - 1]:
        if fmt[i] == "c":
            result *= 25
        else:
            result *= 9
    else:
        if fmt[i] == "c":
            result *= 26
        else:
            result *= 10

print(result)
