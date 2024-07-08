import sys
input = sys.stdin.readline

original = {
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop",
}

n = int(input())
result = True

for i in range(n):
    if input().strip() not in original: result = False

print("No" if result else "Yes")
