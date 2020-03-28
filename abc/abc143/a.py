import sys


def main():
    a, b = [int(s) for s in sys.stdin.readline().strip().split()]

    print(max(a - 2 * b, 0))



main()
