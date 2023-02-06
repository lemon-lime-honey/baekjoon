number = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 
          5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j'}

def solution(age):
    answer = list()
    
    while age:
        answer.append(number[age % 10])
        age //= 10
    
    return (''.join(answer[::-1]))