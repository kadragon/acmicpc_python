import sys

scan: str = lambda: sys.stdin.readline().strip()

A = int(scan())
B = int(scan())

print(A * B)
