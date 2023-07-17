def solution(n, control):
    for letter in control:
        if letter == 'w':
            n += 1
        elif letter == 'a':
            n -= 10
        elif letter == 's':
            n -= 1
        elif letter == 'd':
            n += 10
    return n