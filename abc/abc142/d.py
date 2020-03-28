import sys
import math


def main():
    a, b = [int(s) for s in sys.stdin.readline().strip().split()]

    def factorize(x):
        ret = set()
        for n in range(2, int(math.sqrt(x))+1):
            if x % n == 0:
                while x % n == 0:
                    x //= n
                ret.add(n)
        if x != 1:
            ret.add(x)
        return ret

    a_primes = factorize(a)
    b_primes = factorize(b)
    shared = a_primes.intersection(b_primes)
    print(len(shared) + 1)


main()
