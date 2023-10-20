from collections import deque
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        a, b = map(int, input().split())
        visited = [False for i in range(10000)]
        que = deque([(a, '')])

        while que:
            num, res = que.popleft()
            if num == b:
                print(res)
                break
            visited[num] = True

            d = (2 * num) % 10000
            if not visited[d]:
                que.append((d, res + 'D'))
                visited[d] = True

            s = 9999 if num == 0 else num - 1
            if not visited[s]:
                que.append((s, res + 'S'))
                visited[s] = True

            l = num // 1000 + (num % 1000) * 10
            if not visited[l]:
                que.append((l, res + 'L'))

            r = (num % 10) * 1000 + num // 10
            if not visited[r]:
                que.append((r, res + 'R'))