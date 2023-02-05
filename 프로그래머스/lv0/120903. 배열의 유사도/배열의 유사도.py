def solution(s1, s2):
    answer = 0
    for letter in s1:
        for let in s2:
            if letter == let:
                answer += 1
    return answer