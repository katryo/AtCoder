import sys
import math


def main():
    h_and_a_s = sys.stdin.readline().strip().split(' ')
    h, a = [int(s) for s in h_and_a_s]

    ans = math.ceil(h/a)
    print(ans)


if __name__ == '__main__':
    main()
