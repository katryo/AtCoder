
import sys
import collections


def main():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    # s = 'strangeorange'
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    res = 0
    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if s[i] == s[j]:
                if j == n-1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j+1]+1
                res = max(res, min(dp[i][j], j-i))
    print(res)


main()
