prime = [True] * 1001
prime[0] = False
prime[1] = False
for i in range(len(prime)):
    if prime[i] == True:
        for j in range(2, int(1000/i)+1):
            prime[i*j] = False
n = int(input())
arr = list(map(int, input().split(' ')))
cnt = 0
for i in range(len(arr)):
    if prime[arr[i]] == True:
        cnt += 1
print(cnt)