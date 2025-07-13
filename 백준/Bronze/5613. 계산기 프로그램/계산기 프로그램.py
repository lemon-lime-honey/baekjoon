result = int(input())

while True:
    ipt = input()
    if ipt == "=":
        print(result)
        break
    temp = int(input())
    match ipt:
        case "+":
            result += temp
        case "-":
            result -= temp
        case "*":
            result *= temp
        case "/":
            result //= temp
