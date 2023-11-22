def solution(s):
    words = {'zero': 0, 'one': 1, 'two': 2,
             'three': 3, 'four': 4, 'five': 5,
             'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    idx = 0
    answer = 0

    while idx < len(s):
        if s[idx].isdigit():
            answer = answer * 10 + int(s[idx])
            idx += 1
            continue
        for i in range(3, 6):
            if s[idx: idx+i] in words:
                answer = answer * 10 + words[s[idx: idx+i]]
                idx += i
                break

    return answer