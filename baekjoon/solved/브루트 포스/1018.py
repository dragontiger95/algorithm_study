# 체스판 다시 칠하기

import sys

# n = row, m = col
n, m = map(int, sys.stdin.readline().split())
min_color = 9999
board = []
for i in range(n):
    board.append(input())
    
color = ['B', 'W']
for r_offset in range(n - 7):
    for c_offset in range(m - 7):
        for i in range(2):
            start_val = color[i]
            cnt = 0
            for r in range(r_offset, r_offset+8):
                for c in range(c_offset, c_offset+8):
                    if (r+c)%2 == 0 and board[r][c] != start_val: cnt+=1
                    elif (r+c)%2 == 1 and board[r][c] == start_val: cnt+=1
            if cnt < min_color:
                min_color = cnt
        
print(min_color)