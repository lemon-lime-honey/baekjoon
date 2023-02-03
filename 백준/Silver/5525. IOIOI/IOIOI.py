n = int(input())
m = int(input())
s = input()
pattern = list()
cnt = 0

for i in range(2 * n + 1):
    if i % 2:
        pattern.append('O')
    else:
        pattern.append('I')

for i in range(m - (2 * n + 1)):
    if s[i:(i + 2 * n + 1)] == ''.join(pattern):
        cnt += 1

print(cnt)