def solution(code):
    mode = 0
    ret = list()
    for index, letter in enumerate(code):
        if letter == '1':
            mode = 0 if mode else 1
        else:
            if mode and index % 2: ret.append(letter)
            elif not mode and not index % 2: ret.append(letter)
    return ''.join(ret) if ret else 'EMPTY'