n = int(input())
a = list(map(int, input().split()))

print("Alice" if n % 2 == 0 else "Bob")
