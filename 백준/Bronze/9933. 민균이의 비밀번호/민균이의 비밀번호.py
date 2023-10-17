words = dict()
result = ''

n = int(input())

for i in range(n):
    ipt = input()
    if ipt not in words:
        words[ipt[::-1]] = ipt
        if ipt == ipt[::-1]: result = ipt
    else: result = ipt

print(len(result), result[(len(result) // 2)])