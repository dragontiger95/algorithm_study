row, col = map(int, input().split())
arr = [[0 for j in range(col)] for i in range(row)]

for i in range(2):
    for r in range(row):
        _row = list(map(int, input().split()))
        for c in range(col):
            arr[r][c] += _row[c]
for r in range(row):
    for c in range(col):
        print(arr[r][c], end=' ')
    print('')