from collections import deque

t = int(input())

for i in range(t):
    s, t = map(str, input().split())
    print(f'#{i + 1}', end = ' ')
    
    if len(s) > len(t):
        longer = deque(s)
        shorter = deque(t)
    else:
        longer = deque(t)
        shorter = deque(s)

    for j in range(len(longer)):
        longer.rotate(1)
        shorter.rotate(1)
        if longer[0] != shorter[0]:
            print('no')
            break
    else:
        print('yes')