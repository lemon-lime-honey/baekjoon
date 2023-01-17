n = int(input())

for i in range(n):
    ipt = input()
    before = ipt[0]
    result = [ipt[0], ]

    for index, letter in enumerate(ipt):
        if letter != before:
            result.append(letter)
            before = ipt[index]

    print(''.join(result))