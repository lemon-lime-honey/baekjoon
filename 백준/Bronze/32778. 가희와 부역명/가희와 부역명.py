ipt = input()

if ipt[-1] == ")":
    names = ipt.split("(")
    print(names[0])
    print(names[1][: len(names[1]) - 1])
else:
    print(ipt)
    print("-")
