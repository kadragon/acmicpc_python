import sys

scan: str = lambda: sys.stdin.readline().strip()


def solve():
    c: int = int(scan())
    str_a: str = scan()
    str_b: str = scan()

    ans: int = 0

    for i in range(c):
        ans += 0 if str_a[i] == str_b[i] else 1

    return ans


def main():
    N: int = int(scan())
    for i in range(1, N+1):
        ans = solve()

        print("Case %d: %d" % (i, ans))


if __name__ == "__main__":
    main()
