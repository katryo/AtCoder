import sys
import collections


def main():
    [n, q] = [int(s) for s in sys.stdin.readline().strip().split()]
    a = [-1] * (n-1)
    b = [-1] * (n-1)
    tree = collections.defaultdict(set)
    for i in range(n-1):
        a[i], b[i] = [int(s) for s in sys.stdin.readline().strip().split()]
        tree[a[i]-1].add(b[i]-1)
        tree[b[i]-1].add(a[i]-1)

    p = [-1] * q
    x = [-1] * q
    adds = [0] * n
    for i in range(q):
        p[i], x[i] = [int(s) for s in sys.stdin.readline().strip().split()]
        adds[p[i]-1] += x[i]

    results = [0] * n
    seen = set()

    # def rec_add(node, cur, c):
    #     if c > 1000:
    #         return
    #     cur += adds[node]
    #     results[node] = cur
    #     seen.add(node)
    #     for child in tree[node]:
    #         if child in seen:
    #             continue
    #         rec_add(child, cur, c+1)
    #
    # rec_add(0, 0, 0)

    for i in range(n):
        results[i] = adds[i]
        for child in tree[i]:
            adds[child] += results[i]
    print(' '.join([str(n) for n in results]))


main()
