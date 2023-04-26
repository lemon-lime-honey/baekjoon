def solution(number):
    if number == 0:
        return ['-']

    temp = solution(number - 1)
    result = list()

    for element in temp:
        result.append(element)
    for element in temp:
        result.append(' ')
    for element in temp:
        result.append(element)
    return result


while True:
    try:
        n = int(input())
        print(''.join(solution(n)))
    except EOFError:
        break