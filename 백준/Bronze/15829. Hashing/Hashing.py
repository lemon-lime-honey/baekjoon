alpha = 'abcdefghijklmnopqrstuvwxyz'
l = int(input())
array = input()
result = 0

for i in range(l):
    for j in range(26):
        if alpha[j] == array[i]:
            result += (j + 1) * 31 ** i

result %= 1234567891

print(result)