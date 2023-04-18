import sys


def scan():
    return sys.stdin.readline().strip().split()


A, B = map(int, scan())
C, D = map(int, scan())

all = [A/C+B/D, C/D+A/B, D/B+C/A, B/A+D/C]

print(all.index(max(all)))
