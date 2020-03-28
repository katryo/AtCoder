import sys


def main():
    h_and_n_s = sys.stdin.readline().strip().split(' ')
    h, n = [int(s) for s in h_and_n_s]
    a = [int(s) for s in sys.stdin.readline().strip().split(' ')]

    if sum(a) >= h:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
