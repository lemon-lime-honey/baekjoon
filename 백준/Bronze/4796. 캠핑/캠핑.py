case_number = 1

while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    print(f'Case {case_number}: ', end = '')
    if (v % p) <= l:
        result = (v // p) * l + (v % p)
    else:
        result = (v // p + 1) * l
    print(result)
    case_number += 1