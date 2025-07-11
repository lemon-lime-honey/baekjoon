n = int(input())
before = input()
after = input()

if n % 2:
    for i in range(len(before)):
        if before[i] == after[i]:
            print("Deletion failed")
            break
    else:
        print("Deletion succeeded")
else:
    if before == after:
        print("Deletion succeeded")
    else:
        print("Deletion failed")
