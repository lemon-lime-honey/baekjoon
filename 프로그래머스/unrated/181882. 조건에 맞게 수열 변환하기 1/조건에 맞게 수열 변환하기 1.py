def solution(arr):
    answer = list()
    for number in arr:
        if number >= 50 and not number % 2:
            answer.append(number // 2)
        elif number < 50 and number % 2:
            answer.append(number * 2)
        else: answer.append(number)
    return answer