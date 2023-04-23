import sys


def scan(): return sys.stdin.readline().strip()


N: int = int(scan())
max_x, max_y, min_x, min_y = -10001, -10001, 10001, 10001

for _ in range(N):
    x, y = map(int, scan().split())
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    min_x = min(min_x, x)
    min_y = min(min_y, y)

print((max_x - min_x) * (max_y - min_y))
