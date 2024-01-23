import re, sys
input = sys.stdin.readline

t = int(input())
pattern = r'^[A-F]?A+F+C+[A-F]?$'

for i in range(t):
    ipt = input().rstrip()
    print('Infected!' if re.match(pattern, ipt) else 'Good')