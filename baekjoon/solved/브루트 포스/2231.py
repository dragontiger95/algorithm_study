n = int(input())
constructor = [0] * 1000001

for num in range(1,999955):
    sum = num
    _num = num
    while _num != 0:
        sum += _num%10
        _num = int(_num/10)
    if constructor[sum] != 0:
        if num < constructor[sum]:
            constructor[sum] = num
    else:
        constructor[sum] = num

print(constructor[n])