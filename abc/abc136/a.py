import sys


def main():
    limit, cur, inc = [int(s) for s in sys.stdin.readline().strip().split()]

    diff = limit - cur
    print(max(inc - diff, 0))


main()
