import sys


def read() -> str: return sys.stdin.readline().strip()
def read_int() -> int: return int(read())
def read_ints() -> list[int]: return list(map(int, read().split()))
def print_out(output: any) -> None: sys.stdout.write(str(output) + "\n")


def main():
    pass


if __name__ == "__main__":
    main()

    sys.stdout.flush()
