scan_ints: list[int] = lambda: list(map(int, input().split()))


def main():
    _, _ = scan_ints()
    a: list[int] = scan_ints()
    b: list[int] = scan_ints()

    diff: list = list(set(a) - set(b))

    print(len(diff))

    if len(diff) > 0:
        diff.sort()
        for i in diff:
            print(i, end=" ")

        print()


if __name__ == "__main__":
    main()
