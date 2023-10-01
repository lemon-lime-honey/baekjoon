s = input()
ref = 0

while ref < len(s):
    if s[ref:ref + 2] == 'pi':
        ref += 2
    elif s[ref:ref + 2] == 'ka':
        ref += 2
    elif s[ref:ref + 3] == 'chu':
        ref += 3
    else:
        break

print('YES' if ref == len(s) else 'NO')