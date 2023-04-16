# 포도주 시식

# 앞선 문제 2579 번과 다른 점 -> 2579 에서는 i 번째 계단을 무조건 밟아야 했지만,
# 이 문제는 i 번째 와인을 무조건 마실 이유가 없음

n = int(input())
dp = [0] * (n+1)

wine = []
wine.append(0)
for i in range(1, n+1):
    wine.append(int(input()))

if n >= 1:
    dp[1] = wine[1]
if n >= 2:
    dp[2] = dp[1] + wine[2]
if n >= 3:
    dp[3] = max(dp[2], dp[1] + wine[3], wine[2] + wine[3])
if n >= 4:
    for i in range(4, n+1):
        dp[i] = max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i])

print(dp[n])