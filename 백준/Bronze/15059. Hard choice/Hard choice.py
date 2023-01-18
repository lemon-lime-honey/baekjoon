ca, ba, pa = map(int, input().split())
cr, br, pr = map(int, input().split())

result = 0

if cr > ca:
    result += cr - ca
if br > ba:
    result += br - ba
if pr > pa:
    result += pr - pa

print(result)