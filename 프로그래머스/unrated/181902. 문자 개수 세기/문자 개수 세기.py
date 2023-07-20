def solution(my_string):
    answer = [0 for i in range(52)]
    for letter in my_string:
        target = ord(letter)
        if target >= 97:
            answer[target - 71] += 1
        elif target >= 65:
            answer[target - 65] += 1
    return answer