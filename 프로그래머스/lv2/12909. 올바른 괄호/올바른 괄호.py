def solution(s):
    stack = list()
    for element in s:
        if element == '(':
            stack.append(element)
        else:
            if not stack:
                return False
            if stack[-1] != '(':
                return False
            stack.pop()
    if not stack:
        return True
    return False