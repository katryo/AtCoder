import sys


def main():
    a1, a2, a3 = [int(s) for s in sys.stdin.readline().strip().split(' ')]
    if a1 + a2 + a3 >= 22:
        print('bust')
    else:
        print('win')


main()
