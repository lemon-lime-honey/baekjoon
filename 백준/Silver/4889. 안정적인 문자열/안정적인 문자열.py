idx = 1

while True:
    ipt = input()
    if ipt[0] == "-":
        break
    stack = list()
    cnt = 0

    for letter in ipt:
        if letter == "{":
            stack.append(letter)
        else:
            if stack:
                stack.pop()
            else:
                stack.append("{")
                cnt += 1

    cnt += len(stack) // 2

    print(f"{idx}. {cnt}")
    idx += 1
