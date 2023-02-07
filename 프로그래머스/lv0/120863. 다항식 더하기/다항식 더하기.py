def solution(polynomial):
    elements = polynomial.split()
    answer = list()
    ex = 0
    number = 0

    for element in elements:
        if element[-1] == 'x':
            try:
                ex += int(element[:-1])
            except:
                ex += 1
        elif element.isdecimal():
            number += int(element)
    
    if not ex:
        answer.append(str(number))
    else:
        if ex == 1:
            answer.append('x')
        else:
            answer.append(str(ex) + 'x')
        if number:
            answer.append('+')
            answer.append(str(number))
    
    return (' '.join(answer))