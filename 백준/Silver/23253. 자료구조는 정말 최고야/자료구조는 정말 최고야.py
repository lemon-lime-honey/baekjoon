import sys

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())

    for i in range(m):
        k = int(input())
        books = list(map(int, input().split()))
        for j in range(k - 1, 0, -1):
            if books[j - 1] < books[j]:
                for l in range(m - i):
                    input()
                print("No")
                return

    print("Yes")
    return


if __name__=="__main__":
    main()