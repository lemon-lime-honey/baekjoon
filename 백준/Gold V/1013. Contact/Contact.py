import re

t = int(input())

for i in range(t):
    print('YES' if re.fullmatch('(100+1+|01)+', input()) else 'NO')