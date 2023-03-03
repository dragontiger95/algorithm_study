ch = [-1] * 26
txt = input()
for i in range(len(txt)):
    if ch[ord(txt[i])-97] == -1:
        ch[ord(txt[i])-97] = i
for i in range(len(ch)):
    if i == len(ch)-1:
        print(ch[i])
    else:
        print(ch[i], end=' ')