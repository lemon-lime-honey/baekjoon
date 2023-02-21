def solution(s):
    p, y = 0, 0
    
    for letter in s:
        if letter in 'Pp':
            p += 1
        elif letter in 'Yy':
            y += 1
    
    if p == y:
        return True
    else:
        return False