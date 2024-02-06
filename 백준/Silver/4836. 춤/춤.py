while True:
    try:
        ipt = input().split()
        res = list()
        rule = list()
        chk = set()
        if ipt[0] == 'jiggle':
            rule.append(4)
        if (len(ipt) < 3 or 
            not (ipt[-3] == 'clap' and 
                 ipt[-2] == 'stomp' and 
                 ipt[-1] == 'clap')):
            rule.append(2)
        for i in range(len(ipt)):
            chk.add(ipt[i])
            if ipt[i] == 'dip':
                if not ((i > 1 and ipt[i - 2] == 'jiggle') or
                        (i > 0 and ipt[i - 1] == 'jiggle') or
                        (i != len(ipt) - 1 and ipt[i + 1] == 'twirl')):
                    rule.append(1)
                    res.append(ipt[i].upper())
                else:
                    res.append(ipt[i])
            else:
                res.append(ipt[i])
        if 'twirl' in chk and 'hop' not in chk:
            rule.append(3)
        if 'dip' not in chk:
            rule.append(5)
        rule.sort()

        if not rule:
            print('form ok:', *res)
        elif len(rule) == 1:
            print(f'form error {rule[0]}:', *res)
        else:
            print('form errors ', end='')
            for i in range(len(rule)):
                if i == len(rule) - 2:
                    print(f'{rule[i]} and ', end='')
                elif i == len(rule) - 1:
                    print(f'{rule[i]}: ', end='')
                else:
                    print(f'{rule[i]}, ', end='')
            print(*res)
    except:
        break