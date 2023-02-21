def solution(seoul):
    for index, element in enumerate(seoul):
        if element == 'Kim':
            x = index
            break

    answer = f'김서방은 {x}에 있다'
    return answer