ipt = input()

if '0' not in ipt: print(-1)
else:
    result = list()
    chk = 0
    for num in ipt:
        chk += int(num)
        result.append(int(num))
    if chk % 3: print(-1)
    else:
        print(*sorted(result, reverse=True), sep='')