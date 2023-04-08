# 정수 삼각형

#       [0]
#     [0] [1]
#    [0] [1] [2]
#   [0] [1] [2] [3]

# floor = [[0]*n]*n 
# --> 이렇게 배열 할당하면 [0,0,0, ... ,0 n개] 가 n 개만큼 생성되지만,
# --> 각 [0,0,0, ... ,0 n개] 가 다 같은 배열 참조하기 때문에 floor[0][0] = 1 하면 floor[1 ~ n-1][0] 모두 1로 바뀜

import sys

n = int(input())
# floor = [[0]*n]*n

floor = []
tri = []
for i in range(n):
    tri.append(list(map(int, sys.stdin.readline().split())))
    floor.append([0]*(i+1))

floor[0][0] = tri[0][0]
for f in range(1,n):
    for i in range(len(tri[f])):
        if i == 0:
            floor[f][i] = floor[f-1][i] + tri[f][i]
        elif i == len(tri[f])-1:
            floor[f][i] = floor[f-1][i-1] + tri[f][i]
        else:
            floor[f][i] = max(floor[f-1][i-1], floor[f-1][i]) + tri[f][i]

print(max(floor[n-1]))