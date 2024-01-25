vowel = 'aiyeou'
consonant = 'bkxznhdcwgpvjqtsrlmf'

while True:
    try:
        target = input()
        result = list()

        for letter in target:
            if not letter.isalpha():
                result.append(letter)
                continue
            cap = False
            if letter.isupper():
                cap = True
            if letter.lower() in vowel:
                idx = vowel.index(letter.lower())
                idx -= 3
                if cap:
                    result.append(vowel[idx].upper())
                    continue
                result.append(vowel[idx])
            else:
                idx = consonant.index(letter.lower())
                idx -= 10
                if cap:
                    result.append(consonant[idx].upper())
                    continue
                result.append(consonant[idx])

        print(''.join(result))
    except:
        break