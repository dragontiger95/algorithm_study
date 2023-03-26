# 재귀의 귀재

n = int(input())
cnt = 0

def isPalindrome(s, l, r):
    global cnt
    cnt += 1
    if l>=r: return 1
    elif s[l] != s[r]: return 0
    else:
        return isPalindrome(s, l+1, r-1)

for i in range(n):
    s = input()
    cnt = 0
    print(isPalindrome(s, 0 ,len(s) - 1), end=' ')
    print(cnt)