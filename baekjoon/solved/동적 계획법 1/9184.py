# 신나는 함수 실행

# 재귀(+memoization) 전혀 안쓰고 오로지 memoization으로만 풀이

import sys

# -50 ~ -1 -> 51 ~ 100
# 0 ~ 50 -> 0 ~ 50
w = [[[-1 for _ in range(101)] for _ in range(101)] for _ in range(101)]

for a in range(-50, 51):
    for b in range(-50, 51):
        for c in range(-50, 51):
            if a < 0 and b < 0 and c < 0:
                w[a+101][b+101][c+101] = 1
            elif a < 0 and b < 0:
                w[a+101][b+101][c] = 1
            elif b < 0 and c < 0:
                w[a][b+101][c+101] = 1
            elif c < 0 and a < 0:
                w[a+101][b][c+101] = 1
            elif a < 0:
                w[a+101][b][c] = 1
            elif b < 0:
                w[a][b+101][c] = 1
            elif c < 0:
                w[a][b][c+101] = 1
            else:
                w[a][b][c] = 1

for b in range(1, 51):
    for c in range(1, 51):
        w[0][b][c] = 1
for a in range(1, 51):
    for c in range(1, 51):
        w[a][0][c] = 1
for a in range(1, 51):
    for b in range(1, 51):
        w[a][b][0] = 1

for a in range(1, 51):
    w[a][0][0] = 1
for b in range(1, 51):
    w[0][b][0] = 1
for c in range(1, 51):
    w[0][0][c] = 1

for a in range(1, 21):
    for b in range(1, 21):
        for c in range(1, 21):
            if a < b and b < c:
                w[a][b][c] = w[a][b][c-1] + w[a][b-1][c-1] - w[a][b-1][c]
            else:
                w[a][b][c] = w[a-1][b][c] + w[a-1][b-1][c] + w[a-1][b][c-1] - w[a-1][b-1][c-1]

for a in range(1, 51):
    for b in range(1, 51):
        for c in range(1, 51):
            if a > 20 or b > 20 or c > 20:
                w[a][b][c] = w[20][20][20]


while(1):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1: break
    
    print('w(%d, %d, %d) = ' % (a,b,c), end='')
    if a < 0 and b < 0 and c < 0:
        print(w[a+101][b+101][c+101])
    elif a < 0 and b < 0:
        print(w[a+101][b+101][c])
    elif b < 0 and c < 0:
        print(w[a][b+101][c+101])
    elif c < 0 and a < 0:
        print(w[a+101][b][c+101])
    elif a < 0:
        print(w[a+101][b][c])
    elif b < 0:
        print(w[a][b+101][c])
    elif c < 0:
        print(w[a][b][c+101])
    else:
        print(w[a][b][c])
