s = input()
s_list = s.split(' ')
s_list = [ele for ele in s_list if ele != '']
print(len(s_list))