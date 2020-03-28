import sys

n = int(sys.stdin.readline().strip())

digits = 0
cur = n
while cur:
    cur //= 10
    digits += 1


dp = [[[0] * 10 for _ in range(2)] for _ in range(digits + 2)]

dp[0][0] = 1

for i in range(1, digits):
    divider = 10 ** (digits - 1 - i)
    digit = (n // divider) % 10
    for j in range(2):
        for k in range(10):
            if j:
                limit = 9
            else:
                limit = digit
            for m in range(limit+1):
                is_small = 1
                if j == 0 and k == digit:
                    is_small = 0

                if m == 1:
                    last = 2
                else:
                    last = m
                dp[i+1][is_small][last] += dp[i][j][k]


