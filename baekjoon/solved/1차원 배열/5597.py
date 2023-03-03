l = []
while(1):
    try:
        a = input()
        if a == "":
            break
        l.append(int(a))
    except EOFError:
        break
for i in range(1,31):
    if l.count(i) == 0:
        print(i)