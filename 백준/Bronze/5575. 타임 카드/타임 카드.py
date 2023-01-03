for i in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    
    t1 = h1 * 60 * 60 + m1 * 60 + s1
    t2 = h2 * 60 * 60 + m2 * 60 + s2
    t = t2 - t1
    
    sec = t % 60
    hour = t // 3600
    min = (t - hour * 3600) // 60
    
    print(f'{hour} {min} {sec}')