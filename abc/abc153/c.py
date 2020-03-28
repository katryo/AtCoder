import sys


def main():
    n_and_k_s = sys.stdin.readline().strip().split(' ')
    n, k = [int(s) for s in n_and_k_s]
    h = [int(s) for s in sys.stdin.readline().strip().split(' ')]

    h.sort(reverse=True)

    total = 0
    special = 0
    for i in range(len(h)):
        if special < k:
            special += 1
            continue
        total += h[i]
    print(total)


if __name__ == '__main__':
    main()
