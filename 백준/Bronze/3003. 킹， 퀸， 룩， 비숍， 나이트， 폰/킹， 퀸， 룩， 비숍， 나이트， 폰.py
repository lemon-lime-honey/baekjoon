full  = [1, 1, 2, 2, 2, 8]
num = list(map(int, input().split()))
result = ''
for i in range(6):
    result += str(full[i] - num[i])
    result += ' '
print(result[:-1])