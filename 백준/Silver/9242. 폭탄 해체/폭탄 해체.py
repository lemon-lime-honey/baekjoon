numdict = {('***', '* *', '* *', '* *', '***'): 0,
           ('  *', '  *', '  *', '  *', '  *'): 1,
           ('***', '  *', '***', '*  ', '***'): 2,
           ('***', '  *', '***', '  *', '***'): 3,
           ('* *', '* *', '***', '  *', '  *'): 4,
           ('***', '*  ', '***', '  *', '***'): 5,
           ('***', '*  ', '***', '* *', '***'): 6,
           ('***', '  *', '  *', '  *', '  *'): 7,
           ('***', '* *', '***', '* *', '***'): 8,
           ('***', '* *', '***', '  *', '***'): 9}

raw = list()
code = list()

for i in range(5):
    ipt = input()
    temp = list()
    j = 0

    while j < len(ipt):
        temp.append(ipt[j:j + 3])
        j += 4

    if raw:
        for j in range(len(temp)):
            raw[j].append(temp[j])
    else:
        for j in range(len(temp)):
            raw.append([temp[j]])

for i in range(len(raw) - 1, -1, -1):
    chk = tuple(raw[i])
    if chk not in numdict:
        print('BOOM!!')
        break
    code.append(numdict[chk])
else:
    result = 0
    for j in range(len(code)):
        result += code[j] * (10 ** j)
    if result % 6: print('BOOM!!')
    else: print('BEER!!')