prime = [True] * 10001
prime[0] = False
prime[1] = False
for i in range(10001):
    if prime[i] == True:
        for j in range(2, int(10000/i)+1):
            prime[i*j] = False
_sum = 0
_min = 99999
start = int(input())
end = int(input())

for i in range(start, end+1):
    if prime[i] == True:
        _sum += i
        if i < _min:
            _min = i
if _sum == 0:
    print(-1)
else:
    print(_sum)
    print(_min)