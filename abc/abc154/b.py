import sys


def main():
    s, t = sys.stdin.readline().strip().split()
    a, b = [int(s) for s in sys.stdin.readline().strip().split()]
    u = sys.stdin.readline().strip()

    if u == s:
        print(a-1, b)
    else:
        print(a, b-1)


if __name__ == '__main__':
    main()