# 연속합
# 다시 풀어볼 문제

# 현재 index까지 최대 합 -> tot[index]
# 이전 index까지 합이 음수만 아니면 현재 최대합 구하는데 영향을 끼치지 않음 -> 10 -10 9 8 7 6 합 == 9 8 7 6 합 --> 10 -11 9 8 7 6 합 < 9 8 7 6 합
# 이전 index까지 합이 음수면 현재 index부터 다시 시작

import sys

n = int(input())

arr = list(map(int, sys.stdin.readline().split()))

tot = [0] * n
tot[0] = arr[0]
for i in range(1, n):
    tot[i] = max(tot[i-1] + arr[i], arr[i])

print(max(tot))
