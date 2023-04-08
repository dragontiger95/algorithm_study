# RGB거리

n = int(input())

home = []
for i in range(n):
    home.append(list(map(int, input().split())))

r = [0] * n
g = [0] * n
b = [0] * n

r[0] = home[0][0]
g[0] = home[0][1]
b[0] = home[0][2]

for i in range(1, n):
    r[i] = min(g[i-1], b[i-1]) + home[i][0]
    g[i] = min(r[i-1], b[i-1]) + home[i][1]
    b[i] = min(r[i-1], g[i-1]) + home[i][2]

print(min(r[n-1],g[n-1],b[n-1]))