n = int(input())
cnt = n

while cnt:
    if cnt > 1:
        print(f"{cnt} bottles of beer on the wall, {cnt} bottles of beer.")
        if cnt > 2:
            print(
                f"Take one down and pass it around, {cnt - 1} bottles of beer on the wall."
            )
        else:
            print("Take one down and pass it around, 1 bottle of beer on the wall.")
    else:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")
    print()
    cnt -= 1

print("No more bottles of beer on the wall, no more bottles of beer.")

if n != 1:
    print(f"Go to the store and buy some more, {n} bottles of beer on the wall.")
else:
    print("Go to the store and buy some more, 1 bottle of beer on the wall.")
