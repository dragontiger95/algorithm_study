# 계단 오르기

# case[i] -> i-2 번까지 최대 + stairs[i-1] + stairs[i] = ...o|xoo
#         OR i-3 번까지 최대 + stairs[i] = ....o|xo
# 마지막 계단은 무조건 밟으므로 stairs[i] 가 포함되는 조건만 계산

n = int(input())
stairs = []
for i in range(n):
    stairs.append(int(input()))

case = [0] * n

if n >= 1:
    case[0] = stairs[0]
if n >= 2:
    case[1] = case[0] + stairs[1]

if n >= 3:
    case[2] = max(case[0] + stairs[2], stairs[1] + stairs[2])
    for i in range(3, n):
        case[i] = max(case[i-3] + stairs[i-1] + stairs[i], case[i-2] + stairs[i])
print(case[n-1])