def solution(s):
    result = list(s[0].upper())
    
    for i in range(1, len(s)):
        if s[i - 1] == " ":
            result.append(s[i].upper())
        else:
            result.append(s[i].lower())
            
    return "".join(result)