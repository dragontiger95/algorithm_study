n = int(input())
cnt = 0
for i in range(n):
    s = input()
    ch = ''
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            ch += s[i-1]
        if i == len(s)-1:
            ch += s[i]
    if len(ch) == len(''.join(set(ch))):
        cnt += 1
print(cnt)