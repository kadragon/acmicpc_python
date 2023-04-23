import sys

scan: int = lambda: int(sys.stdin.readline().strip())


for _ in range(3):
    ans = 0
    N = scan()
    for _ in range(N):
        ans += scan()

    if ans > 0:
        print("+")
    elif ans < 0:
        print("-")
    else:
        print(0)
