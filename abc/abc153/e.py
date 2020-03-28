import sys

def main():
    h_and_n_s = sys.stdin.readline().strip().split(' ')
    h, n = [int(s) for s in h_and_n_s]
    a = [-1] * n
    b = [-1] * n

    # max_a = 0
    # ef_i = -1
    for i in range(n):
        a[i], b[i] = [int(s) for s in sys.stdin.readline().strip().split(' ')]
        # max_a = max(max_a, a[i])
        # if a[ef_i] / b[ef_i] < a[i] / b[i]:
        #     ef_i = i

    dp = [float('inf')] * (h+1)

    for point in range(h+1):
        for i in range(n):
            if point <= a[i]:
                dp[point] = min(dp[point], b[i])
                continue

            dp[point] = min(dp[point], dp[point-a[i]] + b[i])

    print(dp[h])


if __name__ == '__main__':
    main()
