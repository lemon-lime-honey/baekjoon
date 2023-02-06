def solution(s):
    target = s.split()
    answer = list()
    
    for element in target:
        if element == "Z":
            try:
                answer.pop()
            except:
                continue
        else:
            answer.append(int(element))
    
    return sum(answer)