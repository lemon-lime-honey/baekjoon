def solution(my_string):
    answer = 0
    length = len(my_string)
    number = list()
    
    for i in range(length):
        if my_string[i].isdigit():
            number.append(my_string[i])
        else:
            if number:
                answer += int(''.join(number))
                number = list()
        if (i == length -1) and number:
            answer += int(''.join(number))
    
    return answer