l = []
while(1):
    try:
        a = input()
        if a == "":
            break
        l.append(int(a))
    except EOFError:
        break
print(max(l))
print(l.index(max(l)) + 1)