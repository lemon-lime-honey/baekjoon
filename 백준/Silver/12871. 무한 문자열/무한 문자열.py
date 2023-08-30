s = input()
t = input()

i, j = 0, 0

while True:
    if s[i] != t[j]:
        print(0)
        break
    if (i == len(s) - 1) and (j == len(t) - 1):
        print(1)
        break
    if (i == len(s) - 1):
        i = 0
        j += 1
    elif (j == len(t) - 1):
        i += 1
        j = 0
    else:
        i += 1
        j += 1