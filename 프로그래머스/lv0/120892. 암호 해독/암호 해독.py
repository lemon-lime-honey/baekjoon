def solution(cipher, code):
    answer = list()
    for index, letter in enumerate(cipher):
        if not ((index + 1) % code):
            answer.append(letter)
    return (''.join(answer))