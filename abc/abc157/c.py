import sys


def main():
    n, m = list(map(int, sys.stdin.readline().strip().split()))

    cur = [-1] * n

    # s = [0] * m
    # c = [0] * m

    for i in range(m):
        s, c = list(map(int, sys.stdin.readline().strip().split()))

        s -= 1

        # 0 in the head. e.g.
        # 3 1
        # 1 0
        if c == 0 and s != n - 1:
            return -1

        if cur[s] == -1:
            cur[s] = c
        else:
            if cur[s] == c:
                continue
            else:
                return -1

    if cur[0] == -1:
        if n > 1:
            cur[0] = 1
    for i in range(n):
        if cur[i] == -1:
            cur[i] = 0

    return ''.join([str(num) for num in cur])


result = main()
print(result)
