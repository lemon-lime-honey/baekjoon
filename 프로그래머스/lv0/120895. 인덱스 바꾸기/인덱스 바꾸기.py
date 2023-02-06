def solution(my_string, num1, num2):
    answer = list()

    for index, letter in enumerate(my_string):
        if index == num1:
            answer.append(my_string[num2])
        elif index == num2:
            answer.append(my_string[num1])
        else:
            answer.append(letter)

    return (''.join(answer))