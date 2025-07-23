t = int(input())

for i in range(1, t + 1):
    b = int(input())
    ipt = input()
    result = list()

    for j in range(b):
        target = list()
        for k in range(8):
            if ipt[j * 8 + k] == "I":
                target.append("1")
            else:
                target.append("0")
        result.append(chr(int("".join(target), 2)))

    print(f"Case #{i}: {''.join(result)}")
