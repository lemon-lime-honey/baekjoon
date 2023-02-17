def hanoi(n, f, t, l):
    if n == 1:
        fList.append(f)
        tList.append(t)
        return
    hanoi(n - 1, f, l, t)
    fList.append(f)
    tList.append(t)
    hanoi(n - 1, l, t, f)

fList = list()
tList = list()
k = int(input())
hanoi(k, 1, 3, 2)

print(2 ** k - 1)
for i in range(2 ** k - 1):
    print(fList[i], tList[i])