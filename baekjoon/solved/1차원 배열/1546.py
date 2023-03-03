n = int(input())
l = list(map(int, input().split()))
_max = max(l)
rev_l = [ele/_max*100 for ele in l]
print(sum(rev_l)/n)