# 문자열 집합

n, m = map(int, input().split())

s = []
comp = []
comp_dict = {}
for i in range(n):
    s.append(input())
for i in range(m):
    word = input()
    comp.append(word)
    if word in comp_dict: comp_dict[word] += 1
    else: comp_dict[word] = 1

s_set = set(s)
comp_set = set(comp)
inter_set = s_set & comp_set

total = 0
for w in inter_set:
    total += comp_dict[w]
print(total)