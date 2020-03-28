import sys


def main():
    n, k = [int(s) for s in sys.stdin.readline().strip().split()]
    h = [int(s) for s in sys.stdin.readline().strip().split()]

    ans = 0
    for hi in h:
        if hi >= k:
            ans += 1
    print(ans)



main()
