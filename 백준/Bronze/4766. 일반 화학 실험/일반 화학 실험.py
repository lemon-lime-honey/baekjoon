before = float(input())

while True:
    now = float(input())
    if now == 999:
        break

    print(f"{now - before:.2f}")
    before = now
