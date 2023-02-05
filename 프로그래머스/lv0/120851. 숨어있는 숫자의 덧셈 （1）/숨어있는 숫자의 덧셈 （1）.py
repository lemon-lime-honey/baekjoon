def solution(my_string):
    answer = 0
    for element in my_string:
        if element.isdecimal():
            answer += int(element)
    return answer