h, m = map(int, input().split())
d = int(input())
tot = 60*h + m
end = tot + d
if end >= 1440:
    print(str(int((end-1440)/60)) + ' ' + str((end-1440)%60))
else:
    print(str(int(end/60)) + ' ' + str(end%60))