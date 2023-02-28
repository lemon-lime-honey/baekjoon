ipt = input()
result = list()
cnt = 0
flag = False

for index, element in enumerate(ipt):
    if element == '.':
        result.append(element)
        if cnt:
            flag = True
    else:
        cnt += 1
        if cnt == 4:
            if result[-1] == 'BB':
                result.pop()
            result.append('AAAA')
            cnt = 0
        elif cnt == 2:
            result.append('BB')
            if index != (len(ipt) - 1):
                if ipt[index + 1] == '.':
                    cnt = 0

if flag or not result or cnt not in (0, 2, 4):
    print(-1)
else:
    print(''.join(result))