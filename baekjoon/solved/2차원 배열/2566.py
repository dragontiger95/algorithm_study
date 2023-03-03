arr = []
_max = -999
for i in range(9):
    row = list(map(int, input().split()))
    arr.append(row)
r = 0
c = 0
for col in range(9):
    for row in range(9):
        if arr[row][col] > _max:
            _max = arr[row][col]
            r = row + 1
            c = col + 1
print(_max)
print("{} {}".format(r, c))