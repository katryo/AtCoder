import sys


def main():
    n, m, l = [int(s) for s in sys.stdin.readline().strip().split()]
    a = [0] * m
    b = [0] * m
    c = [0] * m
    for i in range(m):
        a[i], b[i], c[i] = [int(s) for s in sys.stdin.readline().strip().split()]

    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    for i in range(m):
        dist[a[i]-1][b[i]-1] = c[i]
        dist[b[i]-1][a[i]-1] = c[i]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

    ldist = [[INF] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dist[i][j] <= l:
                ldist[i][j] = 1

    for i in range(n):
        for j in range(n):
            for k in range(n):
                ldist[j][k] = min(ldist[j][k], ldist[j][i] + ldist[i][k])

    q = int(sys.stdin.readline().strip())
    s = [0] * q
    t = [0] * q
    for i in range(q):
        s[i], t[i] = [int(s) for s in sys.stdin.readline().strip().split()]

    for i in range(q):
        s0, t0 = s[i] - 1, t[i] - 1
        if ldist[s0][t0] == INF:
            print(-1)
        else:
            print(ldist[s0][t0]-1)


main()
