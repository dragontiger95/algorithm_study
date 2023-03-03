s = input()
s = s.upper()
ch = [0] * 26
for i in range(len(s)):
    ch[ord(s[i])-65] += 1
max_ch = [idx for idx, ele in enumerate(ch) if ele == max(ch)]
if len(max_ch) > 1:
    print('?')
else:
    print(chr(max_ch[0]+65))