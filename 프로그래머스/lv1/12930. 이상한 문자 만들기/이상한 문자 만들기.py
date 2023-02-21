def solution(s):
    words = s.split(' ')
    answer = list()
    
    for word in words:
        temp = list()
        for index, letter in enumerate(word):
            if index % 2:
                temp.append(letter.lower())
            else:
                temp.append(letter.upper())
        answer.append(''.join(temp))

    return (' '.join(answer))