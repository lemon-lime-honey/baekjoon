def solution(array, height):
    answer = 0
    for element in array:
        if element > height:
            answer += 1
    return answer