ipt = input()
target = {'M', 'O', 'B', 'I', 'S'}

for letter in ipt:
    if letter in target:
        target.remove(letter)

print('NO' if len(target) else 'YES')