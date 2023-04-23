import sys

scan: str = lambda: sys.stdin.readline().strip()

n = int(scan())
ans = 1

for i in range(1, n+1):
    ans *= i

print(ans)
