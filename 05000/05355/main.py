import sys

scan: str = lambda: sys.stdin.readline().strip()


def solve():
    d = scan().split()
    d[0] = float(d[0])

    for c in d[1:]:
        if c == '@':
            d[0] *= 3
        elif c == '%':
            d[0] += 5
        elif c == '#':
            d[0] -= 7

    print("%.2f" % d[0])


N = int(scan())
for _ in range(N):
    solve()
