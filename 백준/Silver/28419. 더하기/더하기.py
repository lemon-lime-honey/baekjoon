def main():
    n = int(input())
    arr = list(map(int, input().split()))

    odd, even = 0, 0

    for i in range(n):
        if i % 2:
            odd += arr[i]
        else:
            even += arr[i]

    if len(arr) == 3 and 0 < (even - odd):
        print(-1)
        return

    print(abs(even - odd))


if __name__ == "__main__":
    main()
