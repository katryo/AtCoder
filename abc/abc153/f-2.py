import sys
import math

def main():
    n_d_a = sys.stdin.readline().strip().split(' ')
    n, d, a = [int(s) for s in n_d_a]
    xh = [[]] * n

    for i in range(n):
        x, h = [int(s) for s in sys.stdin.readline().strip().split(' ')]
        xh[i] = [x, h]
    # n = 3
    # d = 1
    # a = 1
    # xh = [[1, 4], [2, 1], [3, 100]]
    xh.sort()

    cur = 0
    right_indices = [0] * n
    for i in range(n):
        cur = max(cur, i)
        x, h = xh[i]
        right_val = x + d * 2
        while cur < n-1 and xh[cur+1][0] <= right_val:
            cur += 1
        right_indices[i] = cur

    imos = [0] * (n+1)
    ans = 0
    for i in range(n):
        if imos[i] < xh[i][1]:
            need = math.ceil((xh[i][1] - imos[i]) / a)
            ans += need
            imos[i] += need * a
            right_idx = right_indices[i]
            imos[right_idx+1] -= need * a
        imos[i+1] += imos[i]
    print(ans)

if __name__ == '__main__':
    main()

