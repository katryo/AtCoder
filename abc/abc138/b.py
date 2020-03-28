import sys


def main():
    n = int(sys.stdin.readline().strip())
    a = [int(s) for s in sys.stdin.readline().strip().split()]
    # a = [1000] * 100

    multi_all = 1
    for ai in a:
        multi_all *= ai

    divider = 0
    for ai in a:
        divider += multi_all / ai

    print(multi_all / divider)


main()
