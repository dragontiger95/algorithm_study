import sys

n = int(input())
arr = []
# 0 ~ 4000 , -4000 ~ -1 -> 4001 ~ 8000
count = [0] * 8001
sum = 0
_min = 5000
_max = -5000

for i in range(n):
    val = int(sys.stdin.readline())
    arr.append(val)
    sum += val
    if val > _max:
        _max = val
    if val < _min:
        _min = val
    if val < 0: count[val+8001] += 1
    else:   count[val] += 1
    
arr.sort()
arr_len = int(len(arr))
count_list = list(filter(lambda x: count[x] == max(count), range(len(count))))
for i in range(len(count_list)):
    if count_list[i] > 4000:
        count_list[i] = count_list[i] - 8001
count_list.sort()

print(round(sum/arr_len))
print(arr[int(arr_len/2)])
if len(count_list) == 1:    print(count_list[0])
else:   print(count_list[1])

print(_max - _min)