l = []
while(1):
    a,b = map(int, input().split())
    if a==0 and b==0:
        break
    l.append(a+b)
for ele in l:
    print(ele)