n = int(input())
l = []
for i in range(n):
    a, b = map(int, input().split())
    l.append(a+b)    
for ele in l:
    print(ele)