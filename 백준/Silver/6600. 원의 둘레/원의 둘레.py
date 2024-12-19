from math import pi, acos, sin
import sys

input = sys.stdin.readline

while True:
    try:
        x1, y1, x2, y2, x3, y3 = map(float, input().split())
        a = (x1 - x2) ** 2 + (y1 - y2) ** 2
        b = (x1 - x3) ** 2 + (y1 - y3) ** 2
        c = (x2 - x3) ** 2 + (y2 - y3) ** 2
        theta = acos((b + c - a) / (2 * (b**0.5) * (c**0.5)))
        r = (a ** 0.5) / (2 * sin(theta))
        print(f"{2 * pi * r:.2f}")
    except:
        break
