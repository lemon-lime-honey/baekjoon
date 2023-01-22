slang = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5'}
ipt = input()

for letter in ipt:
    if letter in slang:
        print(slang[letter], end = '')
    else:
        print(letter, end = '')