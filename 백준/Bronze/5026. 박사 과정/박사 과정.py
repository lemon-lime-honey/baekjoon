n = int(input())

for i in range(n):
    ipt = input().split("+")
    if len(ipt) == 1:
        print("skipped")
    else:
        print(int(ipt[0]) + int(ipt[1]))
