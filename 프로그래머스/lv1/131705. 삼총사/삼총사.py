def solution(number):
    answer = 0
    
    for i in range(len(number)):
        total = number[i]
        for j in range(i + 1, len(number)):
            total += number[j]
            for k in range(j + 1, len(number)):
                total += number[k]
                if not total:
                    answer += 1
                total -= number[k]
            total -= number[j]
    
    return answer