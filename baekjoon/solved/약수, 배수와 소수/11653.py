prime = [True] * 5001
prime[0] = False
prime[1] = False
for i in range(5001):
    if prime[i] == True:
        for j in range(2, int(5000/i)+1):
            prime[i*j] = False
n = int(input())
num = 2
while n!=1:
    if n%num == 0:
        n = n/num
        print(num)
    else:
        num += 1