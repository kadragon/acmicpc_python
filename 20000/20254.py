import sys


def scan():
    return sys.stdin.readline().strip().split()


def solve():
    ur, tr, ui, to = map(int, scan())
    print(ur * 56 + tr * 24 + ui * 14 + to * 6)


solve()
