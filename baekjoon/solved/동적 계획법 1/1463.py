# 1로 만들기

n = int(input())

dp = [0] * 1000001

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n+1):
    if i % 3 !=0 and i % 2 !=0:
        dp[i] = dp[i-1] + 1
    elif i % 3 != 0 and i % 2 == 0:
        dp[i] = min(dp[i-1]+1, dp[int(i/2)]+1)
    elif i % 3 == 0 and i % 2 != 0:
        dp[i] = min(dp[i-1]+1, dp[int(i/3)]+1)
    elif i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[int(i/3)]+1, dp[int(i/2)]+1, dp[i-1]+1)

print(dp[n])