import sys


def main():
    n = int(sys.stdin.readline().strip())
    v = [int(s) for s in sys.stdin.readline().strip().split()]

    v.sort()

    cur = v[0]
    for i in range(1, len(v)):
        cur = (cur + v[i]) / 2
    print(cur)


main()
