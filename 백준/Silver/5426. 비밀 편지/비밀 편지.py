t = int(input())

for i in range(t):
    ipt = input()
    n = int(len(ipt) ** 0.5)
    letter = list()
    for j in range(0, len(ipt), n):
        letter.append(list(ipt[j: j + n]))
    result = list(zip(letter))
    for j in range(n - 1, -1, -1):
        for k in range(n):
            print(result[k][0][j], end="")
    print()
