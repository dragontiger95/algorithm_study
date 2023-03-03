import sys

n, x = map(int, input().split())
l = list(map(int, sys.stdin.readline().split()))
cnt = 0
ans = []
for ele in l:
    if ele < x:
        ans.append(ele)
for ele in ans:
    print(ele, end=' ')
print()