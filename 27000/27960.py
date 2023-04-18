import sys


def scan():
    return sys.stdin.readline().strip().split()


def solve():
    a, b = map(int, scan())
    print(a ^ b)


solve()
