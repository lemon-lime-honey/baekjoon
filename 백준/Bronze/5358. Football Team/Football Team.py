while True:
    try:
        string = list(input())
        for index, letter in enumerate(string):
            if letter == 'i':
                string[index] = 'e'
            elif letter == 'e':
                string[index] = 'i'
            elif letter == 'I':
                string[index] = 'E'
            elif letter == 'E':
                string[index] = 'I'
        print(''.join(string))
    except:
        break