#설탕 배달

n = int(input())
greedy = 0

while(1):
    if n == 0: break
    if (0 < n and n < 3):
        greedy = -1
        break
    if n%5 == 0:
        greedy += int(n/5)
        break
    else:
        n -= 3
        greedy += 1

print(greedy)