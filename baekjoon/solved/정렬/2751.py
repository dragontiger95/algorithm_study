import sys

# 100만개 입력 속도 고려해야함
n = int(input())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
for i in range(n):
    print(arr[i])