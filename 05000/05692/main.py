import sys


def read_int() -> int: return int(sys.stdin.readline().strip())
def print_out(output: any) -> None: sys.stdout.write(str(output) + "\n")


def main():
    while True:
        n: int = read_int()

        if n == 0:
            break

        ans, k, p = 0, 1, 2

        while n > 0:
            ans += (n % 10) * k
            n //= 10
            k *= p
            p += 1

        print_out(ans)


if __name__ == "__main__":
    main()

    sys.stdout.flush()
