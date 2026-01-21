n = int(input())
flag = False

for i in range(n):
    ipt = input().split()
    if not flag:
        if ipt[1] == "2026":
            print(ipt[0])
            flag = True
