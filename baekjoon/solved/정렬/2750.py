# bubble sort
n = int(input())
arr = []
for i in range(n):
    val = int(input())
    arr.append(val)
for start in range(1, n):
    for i in range(n-1, start-1, -1):
        if arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
for ele in arr:
    print(ele)