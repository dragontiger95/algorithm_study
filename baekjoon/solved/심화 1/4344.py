c = int(input())
for i in range(c):
    l = list(map(int, input().split()))
    tot = sum(l) - l[0]
    avg = int(tot / l[0])
    l.pop(0)
    over_avg_l = [ele for ele in l if ele > avg]
    print('{:.3f}%'.format(len(over_avg_l)/len(l)*100))