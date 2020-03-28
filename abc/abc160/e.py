import sys


def main():
    x, y, a, b, c = [int(s) for s in sys.stdin.readline().strip().split()]
    p = [int(s) for s in sys.stdin.readline().strip().split()]
    q = [int(s) for s in sys.stdin.readline().strip().split()]
    r = [int(s) for s in sys.stdin.readline().strip().split()]

    p.sort(reverse=True)
    q.sort(reverse=True)
    r.sort(reverse=True)

    p = p[:x]
    q = q[:y]

    combined = p + q + r
    combined.sort(reverse=True)
    print(sum(combined[:x+y]))

main()
