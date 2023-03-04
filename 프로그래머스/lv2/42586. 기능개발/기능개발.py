from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = list()
    
    while progresses:
        cnt = 0

        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        while progresses:
            if progresses[0] >= 100:
                cnt += 1
                progresses.popleft()
                speeds.popleft()
            else:
                if cnt:
                    answer.append(cnt)
                break
        
        if not progresses and cnt:
            answer.append(cnt)
    
    return answer