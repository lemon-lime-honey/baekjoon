import sys

n = int(sys.stdin.readline())
ref = 0
result = list()
num = list()
flag = True

for i in range(n):
    ipt = int(sys.stdin.readline())
    while True:
        if len(num) != 0:
            if num[-1] == ipt:
                temp = num.pop()
                if ref < temp:
                    ref = temp
                result.append('-')
                break
        if ref + 1 < ipt + 1:
            for j in range(ref + 1, ipt + 1):
                num.append(j)
                result.append('+')
        else:
            flag = False
            break

if flag:
    for element in result:
        print(element)
else:
    print('NO')