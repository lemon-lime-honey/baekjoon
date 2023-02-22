def solution(s, n):
    answer = list()

    for letter in s:
        if letter.isalpha():
            temp = ord(letter)
            if letter.isupper():
                if temp + n <= 90:
                    answer.append(chr(temp + n))
                else:
                    answer.append(chr(temp + n - 26))
            else:
                if temp + n <= 122:
                    answer.append(chr(temp + n))
                else:
                    answer.append(chr(temp + n - 26))
        else:
            answer.append(letter)

    return (''.join(answer))