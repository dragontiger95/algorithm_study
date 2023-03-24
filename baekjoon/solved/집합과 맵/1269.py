# 대칭 차집합

a, b = map(int, input().split())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_set = set(A_list)
B_set = set(B_list)

inter_set = A_set & B_set
res_set = (A_set | B_set) - inter_set
print(len(res_set))