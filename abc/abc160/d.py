import sys


def main():
    n, x, y = [int(s) for s in sys.stdin.readline().strip().split()]
    x1 = x-1
    y1 = y-1

    score = {i:0 for i in range(n)}

    for i in range(n-1):
        for j in range(i+1, n):
            diff = j - i
            cand = abs(x1 - i) + 1 + abs(y1 - j)
            cand2 = abs(y1 - i) + 1 + abs(x1 - j)
            result = min(diff, cand, cand2)
            score[result] += 1

    for i in range(1, n):
        print(score[i])

main()
