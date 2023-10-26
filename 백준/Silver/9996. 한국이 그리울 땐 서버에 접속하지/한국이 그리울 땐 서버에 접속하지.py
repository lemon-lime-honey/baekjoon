import re

n = int(input())
raw_pattern = '.*'.join(input().split('*'))
pattern = re.compile('^' + raw_pattern + '$')

for i in range(n):
    chk = re.match(pattern, input())
    print("DA" if chk else "NE")