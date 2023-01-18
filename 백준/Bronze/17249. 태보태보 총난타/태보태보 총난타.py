taebo = input()
cnt = 0
for item in taebo:
    if item == '(':
        print(cnt, end = ' ')
        cnt = 0
    elif item == '@':
        cnt += 1
print(cnt)