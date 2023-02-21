number = {i: 0 for i in range(10)}

def solution(numbers):
    answer = 0

    for element in numbers:
        number[element] += 1

    for key, value in number.items():
        if not value:
            answer += key

    return answer