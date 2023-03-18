# 블랙잭

import sys

_max = -999999
n, m = map(int, input().split())
card = list(map(int, sys.stdin.readline().split()))

def black_jack(depth, sum, start):
    global _max
    if depth > 3 or sum > m:    return
    elif depth == 3:
        if _max < sum:  _max = sum
    else:
        for i in range(start, len(card)):
            black_jack(depth+1, sum + card[i], i+1)

black_jack(0,0,0)

print(_max)