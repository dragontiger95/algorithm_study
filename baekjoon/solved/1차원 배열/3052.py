l = []
while(1):
    try:
        a = input()
        if a == "":
            break
        l.append(int(a)%42)
    except EOFError:
        break
distinct = set(l)
print(len(distinct))