k = int(input())

for i in range(1, k + 1):
    h = int(input())
    ipt = input()

    for w in ipt:
        if w == "c":
            h += 1
        else:
            h -= 1

    print(f"Data Set {i}:")
    print(h)
    print()
