while True:
    n = int(input())
    if n == 0:
        break

    result = 0

    for i in range(n):
        ipt = input()
        if len(ipt) < result:
            continue

        for letter in ipt[result:]:
            if letter == " ":
                break
            result += 1

    print(result + 1)
