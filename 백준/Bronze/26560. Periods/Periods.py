n = int(input())

for i in range(n):
    ipt = input()
    if ipt[-1] != ".":
        print(ipt, ".", sep="")
    else:
        print(ipt)
