h, m = map(int, input().split())
tot = 60*h + m
if tot - 45 < 0:
    diff = 45 - tot
    new_tot = 1440 - diff
    print(str(int(new_tot/60)) + ' ' + str(new_tot%60))
else:
    print(str(int((tot-45)/60)) + ' ' + str((tot-45)%60))