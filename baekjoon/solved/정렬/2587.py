n = 5
arr = []
sum = 0
for i in range(n):
    arr.append(int(input()))
    sum += arr[i]
arr.sort()
print(int(sum/n))
print(arr[2])