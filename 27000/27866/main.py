import sys

scan: str = lambda: sys.stdin.readline().strip()

S = scan()
i = int(scan())

print(S[i-1])
