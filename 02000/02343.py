import sys


def input():
    return sys.stdin.readline().strip().split()


n, m = map(int, input())
lecture_legnths = list(map(int, input()))

left, right = max(lecture_legnths), sum(lecture_legnths)

while left < right:
    mid = (left + right) // 2
    cnt = 1
    curr_sum = 0
    for length in lecture_legnths:
        if curr_sum + length > mid:
            cnt += 1
            curr_sum = length
        else:
            curr_sum += length
    if cnt <= m:
        right = mid
    else:
        left = mid + 1

print(left)
