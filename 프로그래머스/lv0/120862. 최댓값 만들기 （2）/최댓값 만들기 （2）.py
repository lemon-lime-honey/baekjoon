def solution(numbers):
    answer = -10 ** 9
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if (i != j) and (numbers[i] * numbers[j] > answer):
                answer = numbers[i] * numbers[j]

    return answer