while True:
    try:
        ipt = input()
        result = [0, 0, 0, 0]
        for letter in ipt:
            if letter.isalnum():
                if letter.islower():
                    result[0] += 1
                elif letter.isupper():
                    result[1] += 1
                elif letter.isnumeric():
                    result[2] += 1
            else:
                result[3] += 1
        print(*result)
    except:
        break