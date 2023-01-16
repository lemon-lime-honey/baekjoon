string = input()
words = list()
temp = list()
flag = 0

for letter in string:
    if letter == '<':
        words.append(''.join(temp))
        temp = list()
        temp.append(letter)
        flag = 1
    elif letter == '>':
        temp.append(letter)
        words.append(''.join(temp))
        temp = list()
        flag = 0
    elif letter == ' ':
        if flag == 0:
            words.append(''.join(temp))
            words.append(letter)
            temp = list()
        else:
            temp.append(letter)
    else:
        temp.append(letter)
words.append(''.join(temp))

for word in words:
    if '<' in word:
        print(word, end = '')
    else:
        print(word[::-1], end = '')
