import sys


def main():
    n = int(sys.stdin.readline().strip())
    if n % 2:
        print(((n + 1) // 2) / n)
    else:
        print(0.5)



main()
