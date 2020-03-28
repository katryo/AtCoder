import sys


def main():
    s = sys.stdin.readline().strip()

    a = []
    for _ in s:
        a.append('x')

    print(''.join(a))


if __name__ == '__main__':
    main()