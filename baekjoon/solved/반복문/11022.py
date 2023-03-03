n = int(input())
a = []
b = []
l = []
for i in range(1, n+1):
    f, s = map(int, input().split())
    a.append(f)
    b.append(s)
    l.append(f+s) 
for i in range(len(l)):
    print('Case #{}: {} + {} = {}'.format(i+1, a[i], b[i], l[i]))