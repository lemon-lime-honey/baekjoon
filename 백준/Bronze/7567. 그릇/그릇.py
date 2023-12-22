ipt = input()
open = False
result = 10

if ipt[0] == '(': open = True

for i in range(1, len(ipt)):
    if (open and ipt[i] == '(' or
        not open and ipt[i] == ')'):
        result += 5
    else:
        result += 10
        open = not open

print(result)