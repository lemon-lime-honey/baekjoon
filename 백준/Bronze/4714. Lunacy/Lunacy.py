while True:
    n = float(input())
    if n < 0:
        break
    print(f'Objects weighing {n:.2f} on Earth will weigh {0.167 * n:.2f} on the moon.')