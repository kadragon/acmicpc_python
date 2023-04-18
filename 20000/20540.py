import sys


def scan():
    return sys.stdin.readline().strip()


def solve():
    mbti = "EISNTFJP"
    r = scan()
    for c in r:
        mbti = mbti.replace(c, "")

    print(mbti)


solve()
