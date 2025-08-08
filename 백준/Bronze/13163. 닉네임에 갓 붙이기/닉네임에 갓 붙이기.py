n = int(input())

for i in range(n):
    ipt = input().split()
    print("god", *ipt[1:], sep="")
