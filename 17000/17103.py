import sys

scan: str = lambda: sys.stdin.readline().strip()


def solve() -> None:
    T: int = int(scan())
    prime: list(int) = [False, True] * 500001
    prime[1] = False
    prime[2] = True

    for i in range(3, int(1000001**0.5)):
        if prime[i]:
            for j in range(i * 2, 1000001, i):
                prime[j] = False

    for _ in range(T):
        N: int = int(scan())
        cnt: int = 0

        for i in range(2, N // 2+1):
            if prime[i] and prime[N - i]:
                cnt += 1

        print(cnt)


solve()
