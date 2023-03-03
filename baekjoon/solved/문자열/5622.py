dial = ['','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
s = input()
sum = 0
for i in range(len(s)):
    for j in range(len(dial)):
        if s[i] in dial[j]:
            sum += (j+1+1)
print(sum)