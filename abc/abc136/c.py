import sys


def main():
    n = int(sys.stdin.readline().strip())
    H = [int(s) for s in sys.stdin.readline().strip().split()]
    if is_possible(n, H):
        print('Yes')
    else:
        print('No')


def is_possible(n, H):
    prev = float('-inf')
    for i in range(n):
        if H[i] - 1 >= prev:
            prev = H[i] - 1
        elif H[i] >= prev:
            prev = H[i]
        else:
            return False
    return True


main()
