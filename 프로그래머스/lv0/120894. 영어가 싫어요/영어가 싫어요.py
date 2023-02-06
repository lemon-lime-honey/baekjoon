def solution(numbers):
    numbers = numbers.replace("one", "1").replace("two", "2")
    numbers = numbers.replace("three", "3").replace("four", "4")
    numbers = numbers.replace("five", "5").replace("six", "6")
    numbers = numbers.replace("seven", "7").replace("eight", "8")
    numbers = numbers.replace("nine", "9").replace("zero", "0")
    answer = int(numbers)

    return answer