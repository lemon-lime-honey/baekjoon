n = int(input())
p = int(input())
case = list()

if n >= 20:
    case.append(int(0.75 * p))
if n >= 15:
    case.append(p - 2000)
if n >= 10:
    case.append(int(0.9 * p))
if n >= 5:
    case.append(p - 500)

try:
    result = min(case)
except:
    result = p

if result < 0:
    print(0)
else:
    print(result)