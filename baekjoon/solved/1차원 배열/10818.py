import sys

n = int(input())
l = list(map(int, sys.stdin.readline().split()))
print(str(min(l)) + ' ' + str(max(l)))