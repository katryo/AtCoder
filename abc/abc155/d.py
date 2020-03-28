import sys

n, k = map(int, sys.stdin.readline().strip().split())
a = map(int, sys.stdin.readline().strip().split())

def main(n, k, a):
    nega = []
    posi = []
    zeros = 0

    for ai in a:
        if ai < 0:
            nega.append(ai)
        elif ai > 0:
            posi.append(ai)
        else:
            zeros += 1

    posi.sort()
    nega.sort(reverse=True)

    ng = - (10 ** 18)-1
    ok = 10 ** 18 + 1

    while ok - ng > 1:
        mid = (ok + ng) // 2
        cnt = 0

        if mid >= 0:
            cnt += zeros * (zeros - 1) // 2 + zeros * (n - zeros)

        if mid > 0:
            cnt += len(nega) * len(posi)
            for a in (posi, nega):
                l = 0
                r = len(a)-1
                while l < r:
                    while l < r and a[l] * a[r] > mid:
                        r -= 1
                    cnt += r - l
                    l += 1
        else:
            r = len(nega) - 1
            for l in range(len(posi)):
                while r >= 0 and posi[l] * nega[r] <= mid:
                    r -= 1
                cnt += len(nega) - r - 1

        if cnt >= k:
            ok = mid
        else:
            ng = mid
    print(ok)


main(n, k, a)