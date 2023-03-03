import sys

n = int(input())
l = list(map(int, sys.stdin.readline().split()))
v = int(input())

print(l.count(v))