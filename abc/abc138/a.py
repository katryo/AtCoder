import sys


def main():
    a = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    if a >= 3200:
        print(s)
    else:
        print('red')

main()
