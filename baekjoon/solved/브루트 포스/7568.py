# 덩치

import sys

n = int(input())
prior = [1] * n
w, h = [0] * n, [0] * n

for i in range(n):
    _w, _h = map(int, sys.stdin.readline().split())
    w[i] = _w
    h[i] = _h

for i in range(n):
    for j in range(n):
        if i == j: continue
        if w[i] < w[j] and h[i] < h[j]:
            prior[i] += 1
for i in range(n):
    print(prior[i], end=' ')
print()