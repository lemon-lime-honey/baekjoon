def solution(keyinput, board):
    answer = [0, 0]
    limitright = (board[0] - 1) // 2
    limitleft = -1 * limitright
    limitup = (board[1] - 1) // 2
    limitdown = -1 * limitup    
    
    for command in keyinput:
        if command == "left":
            answer[0] -= 1
        elif command == "right":
            answer[0] += 1
        elif command == "up":
            answer[1] += 1
        elif command == "down":
            answer[1] -= 1
        
        if answer[0] > limitright:
            answer[0] = limitright
        if answer[0] < limitleft:
            answer[0] = limitleft
        if answer[1] > limitup:
            answer[1] = limitup
        if answer[1] < limitdown:
            answer[1] = limitdown

    return answer