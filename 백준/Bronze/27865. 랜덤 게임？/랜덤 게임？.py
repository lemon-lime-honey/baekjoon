import sys
from random import randint

input = sys.stdin.readline

n = int(input())

while True:
    x = randint(1, n)

    print(f"? {x}")
    sys.stdout.flush()
    ipt = input().strip()

    if ipt == "Y":
        print(f"! {x}")
        break
