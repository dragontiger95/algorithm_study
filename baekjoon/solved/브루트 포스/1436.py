# 영화감독 숌

n = int(input())
series = [0] * n
count = 0
for num in range(5000000):
    if '666' in str(num):
        series[count] = num
        count += 1
    if count == n:
        break

print(series[count - 1])