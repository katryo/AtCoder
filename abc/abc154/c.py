import sys


def main():
    n = int(sys.stdin.readline().strip())
    a = [int(s) for s in sys.stdin.readline().strip().split()]

    seen = set()
    is_yes = True
    for ai in a:
        if ai in seen:
            is_yes = False
            break
        seen.add(ai)
    if is_yes:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()