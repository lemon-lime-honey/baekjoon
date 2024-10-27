socks = set()

for i in range(5):
    num = int(input())
    if num not in socks:
        socks.add(num)
    else:
        socks.discard(num)

print(socks.pop())