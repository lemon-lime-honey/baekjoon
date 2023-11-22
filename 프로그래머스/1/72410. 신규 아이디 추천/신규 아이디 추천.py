def solution(new_id):
    first = new_id.lower()
    second = list()

    for letter in first:
        if letter.isalnum() or letter in ('-_.'):
            second.append(letter)

    answer = list()

    for letter in second:
        if letter != '.' and len(answer) != 0 and answer[-1] == '.':
            while answer and answer[-1] == '.':
                answer.pop()
            answer.append('.')
            answer.append(letter)
            continue
        answer.append(letter)

    if answer and answer[0] == '.':
        answer.pop(0)

    while answer and answer[-1] == '.':
        answer.pop()

    if not answer:
        answer.append('a')

    while len(answer) > 15:
        answer.pop()

    if answer[-1] == '.':
        answer.pop()

    if len(answer) < 3:
        while len(answer) < 3:
            answer.append(answer[-1])

    return ''.join(answer)