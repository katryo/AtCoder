import sys


def main():
    n, k = [int(s) for s in sys.stdin.readline().strip().split()]
    p = [int(s) for s in sys.stdin.readline().strip().split()]

    pd = [0.0] * n
    for i in range(n):
        tot = (p[i] + 1) * p[i] // 2
        ex = tot / p[i]
        pd[i] = ex

    cand = sum(pd[:k])
    ans = cand
    for i in range(k, n):
        cand += pd[i]
        cand -= pd[i-k]
        ans = max(ans, cand)
    print(ans)


if __name__ == '__main__':
    main()