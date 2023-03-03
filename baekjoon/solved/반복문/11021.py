n = int(input())
l = []
for i in range(1, n+1):
    a, b = map(int, input().split())
    l.append(a+b) 
for i in range(len(l)):
    print('Case #{}: {}'.format(i+1, l[i]))