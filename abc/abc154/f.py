import sys


def main():
    r1, c1, r2, c2 = [int(s) for s in sys.stdin.readline().strip().split()]
    MOD = 10 ** 9 + 7
    ans = 0
    dp = [[0] * (c2+1) for _ in range(r2+1)]

    for i in range(r2+1):
        for j in range(c2+1):
            if i == 0 and j == 0:
                dp[0][0] = 1
            else:
                if i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
            if r1 <= i <= r2 and c1 <= j <= c2:
                ans += dp[i][j]
                ans %= MOD
    dp[i][j] = dp[i][j-1] + dp[i-1][j]

    def stair(num):
        num * (num+1) // 2
        

    # row[r2]



    for row in dp:
        print(row)
    print(ans)

if __name__ == '__main__':
    main()