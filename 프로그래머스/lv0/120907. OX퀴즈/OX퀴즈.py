def solution(quiz):
    answer = list()

    for equation in quiz:
        elements = equation.split()
        result = eval(''.join(elements[:-2]))
    
        if result == int(elements[-1]):
            answer.append("O")
        else:
            answer.append("X")

    return answer