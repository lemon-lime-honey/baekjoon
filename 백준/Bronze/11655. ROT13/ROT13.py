string = input()
for letter in string:
    if letter.isalpha():
        temp = ord(letter)
        if letter.isupper():
            if temp <= 77:
                print(chr(temp + 13), end = '')
            else:
                print(chr(temp - 13), end = '')
        else:
            if temp <= 109:
                print(chr(temp + 13), end = '')
            else:
                print(chr(temp - 13), end = '')
    else:
        print(letter, end = '')