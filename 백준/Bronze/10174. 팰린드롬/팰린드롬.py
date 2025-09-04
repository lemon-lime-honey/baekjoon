n = int(input())
for i in range(n):
    ipt = input().lower()
    if ipt == ipt[::-1]:
        print("Yes")
    else:
        print("No")
