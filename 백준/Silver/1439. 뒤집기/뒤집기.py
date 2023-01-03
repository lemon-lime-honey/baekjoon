s = input()
check0 = 0
check1 = 0
if (s[0] == '0'):
    check0 += 1
else:
    check1 += 1
for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        if (s[i] == '0'):
            check0 += 1
        else:
            check1 += 1
print(min(check0, check1))