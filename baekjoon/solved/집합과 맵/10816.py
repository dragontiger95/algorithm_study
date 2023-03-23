# 숫자 카드 2

import sys

# 0 ~ 10,000,000 , 10,000,001 ~ 20,000,000 (-10,000,000 ~ -1) + 20,000,001
exist = [0] * 20000001

n = int(input())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(input())
m_list = list(map(int, sys.stdin.readline().split()))

for num in n_list:
    if num < 0: exist[num + 20000001] += 1
    else: exist[num] += 1

for num in m_list:
    if num < 0: print(exist[num + 20000001], end=' ')
    else: print(exist[num], end=' ')
print()