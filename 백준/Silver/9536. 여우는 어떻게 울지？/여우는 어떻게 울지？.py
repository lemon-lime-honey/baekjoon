t = int(input())

for i in range(t):
    sounds = input().split()
    soundSet = set()
    result = list()

    while True:
        ipt = input()
        if ipt == 'what does the fox say?':
            break
        temp = ipt.split()
        soundSet.add(temp[-1])
 
    for sound in sounds:
        if sound in soundSet:
            continue
        result.append(sound)

    print(*result)