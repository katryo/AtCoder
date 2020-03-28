import sys


def main():
    h = int(sys.stdin.readline().strip())

    def solve(point):
        if point == 1:
            return 1
        return 1 + 2 * solve(point // 2)

    print(solve(h))


if __name__ == '__main__':
    main()
