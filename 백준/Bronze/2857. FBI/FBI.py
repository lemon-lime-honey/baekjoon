import re

pattern = r'FBI'
found = list()

for i in range(1, 6):
    code = input()
    if re.search(pattern, code):
        found.append(str(i))

if found:
    print(' '.join(found))
else:
    print('HE GOT AWAY!')