import sys

scan: str = lambda: sys.stdin.readline().strip()


def main():
    N: int = int(scan())
    min_time: int = 1001

    for _ in range(N):
        A, B = map(int, scan().split())
        min_time = min_time if B < A else min(min_time, B)

    print(min_time if min_time != 1001 else -1)


if __name__ == "__main__":
    main()
