def convert(s):
    zero = s.count("0")
    one = bin(s.count("1"))[2:]
    return (zero, one)

def solution(s):
    answer = [0, 0]

    while s != "1":
        n, s = convert(s)
        answer[0] += 1
        answer[1] += n
        
    return answer