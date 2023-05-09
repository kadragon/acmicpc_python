import sys


def read() -> str: return sys.stdin.readline().strip()
def read_int() -> int: return int(read())
def read_ints() -> list[int]: return list(map(int, read().split()))
def print_out(output) -> None: sys.stdout.write(str(output) + "\n")


def main():
    n, m = read_ints()
    p = [read_int() for _ in range(m)]
    p.sort(reverse=True)

    ans = [0, 0]

    for i in range(min(n, m)):
        benefit = p[i] * (i + 1)
        if ans[1] < benefit:
            ans = [p[i], benefit]

    print_out(f"{ans[0]} {ans[1]}")


if __name__ == "__main__":
    main()
    sys.stdout.flush()
