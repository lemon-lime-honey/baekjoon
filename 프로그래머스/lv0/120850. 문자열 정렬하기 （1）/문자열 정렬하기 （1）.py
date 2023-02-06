def solution(my_string):
    answer = list()

    for element in my_string:
        if element.isdigit():
            answer.append(int(element))

    answer.sort()

    return answer