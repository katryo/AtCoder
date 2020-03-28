import sys


def main():
    n = int(sys.stdin.readline().strip())
    l = [int(s) for s in sys.stdin.readline().strip().split()]
    # n = 4
    # l = [1, 2, 3, 4]

    l.sort()

    # [lo, hi)
    # Returns -1 if no valid item
    def b_search(lo, hi, limit):
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if l[mid] < limit:
                lo = mid
            else:
                hi = mid
        if lo >= hi:
            return -1
        if lo + 1 == hi:
            return lo

    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            a_plus_b = l[i] + l[j]
            valid_longest_idx = b_search(j, n, a_plus_b)
            ans += valid_longest_idx - j

    print(ans)


main()
