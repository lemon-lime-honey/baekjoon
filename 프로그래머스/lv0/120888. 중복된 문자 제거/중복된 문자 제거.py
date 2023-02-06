def solution(my_string):
    letter_set = set()
    answer = list()
    
    for letter in my_string:
        if letter not in letter_set:
            answer.append(letter)
            letter_set.add(letter)
    
    return (''.join(answer))