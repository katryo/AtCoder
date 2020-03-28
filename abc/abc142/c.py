import sys


def main():
    n = int(sys.stdin.readline().strip())
    a = [int(s) for s in sys.stdin.readline().strip().split()]

    tuples = []
    for i in range(n):
        ai = a[i]
        tuples.append((ai, i+1))
    tuples.sort()
    ans_list = [str(tup[1]) for tup in tuples]
    print(' '.join(ans_list))


main()
