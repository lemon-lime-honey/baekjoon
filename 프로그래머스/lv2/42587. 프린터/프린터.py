from collections import deque

def solution(priorities, location):
    printer_que = deque()
    order = 0
    
    for i in range(len(priorities)):
        printer_que.append((priorities[i], i))

    while True:
        ref = max(printer_que)
        now = printer_que.popleft()
        if now[0] == ref[0]:
            order += 1
            if now[1] == location:
                return order
        else:
            printer_que.append(now)