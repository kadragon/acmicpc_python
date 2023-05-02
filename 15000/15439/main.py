import sys

scan: str = lambda: sys.stdin.readline().strip()


def main():
    N: int = int(scan())

    print(N * (N - 1))


if __name__ == "__main__":
    main()
