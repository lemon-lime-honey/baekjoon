ipt = input()

if ipt[0] == ipt[-1] == '"' and len(ipt) > 2:
    print(ipt[1:-1])
else:
    print("CE")
