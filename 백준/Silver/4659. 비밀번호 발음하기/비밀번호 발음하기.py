consonant = 'bcdfghjklmnpqrstvwxyz'
vowel = 'aeiou'
yn = {0: 'acceptable', 1: 'not acceptable'}

while True:
    case = input()
    if case == 'end':
        break
    one = 0
    c_count = 0
    v_count = 0
    last = ''
    flag = 0
    for letter in case:
        if (letter == last) * (letter not in 'eo'):
            flag = 1
            break
        if letter in vowel:
            if v_count == 2:
                flag = 1
                break
            one += 1
            v_count += 1
            c_count = 0
            last = letter
        else:
            if c_count == 2:
                flag = 1
                break
            v_count = 0
            c_count += 1
            last = letter
    if one == 0:
        flag = 1
    print(f'<{case}> is {yn[flag]}.')