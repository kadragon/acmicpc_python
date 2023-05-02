scan_int: int = lambda: int(input())


def main():
    N: int = scan_int()
    ans: int = 0

    for i in range(1, N + 1):
        if i * i <= N:
            ans += 1
        else:
            break

    print(ans)


if __name__ == "__main__":
    main()
