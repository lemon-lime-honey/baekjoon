sel = list(map(int, input().split()))
result = 5000

for num in sel:
    match num:
        case 1:
            if result >= 500:
                result -= 500
        case 2:
            if result >= 800:
                result -= 800
        case 3:
            if result >= 1000:
                result -= 1000

print(result)
