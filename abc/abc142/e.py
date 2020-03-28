import sys


def main():
    n, m = [int(s) for s in sys.stdin.readline().strip().split()]
    a = [0] * m
    c = [0] * m
    inf = float('inf')

    for i in range(m):
        ai, bi = [int(s) for s in sys.stdin.readline().strip().split()]
        a[i] = ai
        ci = [int(s)-1 for s in sys.stdin.readline().strip().split()]
        # print(ci)
        c_val = sum([2 ** num for num in ci])
        c[i] = c_val

    dp = [[inf] * (2 ** n) for _ in range(m)]
    for i in range(m):
        dp[i][0] = 0

    for j in range(2 ** n):
        first_key_boxes = c[0]
        if first_key_boxes & j == j:
            dp[0][j] = a[0]

    for i in range(1, m):
        for j in range(1, 2 ** n):
            prev = j & (~c[i])
            dp[i][j] = min(dp[i-1][j], a[i] + dp[i-1][prev])
    if dp[m-1][2**n-1] == inf:
        print(-1)
    else:
        print(dp[m-1][2**n-1])


main()
