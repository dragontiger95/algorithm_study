paper = [[0 for col in range(101)] for row in range(101)]
# paper = [[0]*101 for row in range(101)]
n = int(input())
for i in range(n):
    col, row = map(int, input().split())
    for r in range(row, row+10):
        for c in range(col, col+10):
            paper[r+1][c+1] = 1
s = 0
for i in paper:
    s += sum(i)
print(s)