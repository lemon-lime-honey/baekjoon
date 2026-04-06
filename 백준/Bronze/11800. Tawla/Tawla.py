name = {
    1: "Yakk", 2: "Doh", 3: "Seh", 4: "Ghar", 5: "Bang", 6: "Sheesh"
}

t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    if b > a:
        a, b = b, a

    if a == 1 and b == 1:
        print(f"Case {i + 1}: Habb Yakk")
    elif a == 2 and b == 2:
        print(f"Case {i + 1}: Dobara")
    elif a == 3 and b == 3:
        print(f"Case {i + 1}: Dousa")
    elif a == 4 and b == 4:
        print(f"Case {i + 1}: Dorgy")
    elif a == 5 and b == 5:
        print(f"Case {i + 1}: Dabash")
    elif a == 6 and b == 5:
        print(f"Case {i + 1}: Sheesh Beesh")
    elif a == 6 and b == 6:
        print(f"Case {i + 1}: Dosh")
    else:
        print(f"Case {i + 1}: {name[a]} {name[b]}")
