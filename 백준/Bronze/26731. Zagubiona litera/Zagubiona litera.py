alpha = list(map(chr, range(65, 91)))

ipt = input()
for letter in alpha:
    if letter not in ipt:
        print(letter)
        break