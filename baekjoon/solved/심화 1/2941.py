cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
ch = input()
for ele in cro:
   ch = ch.replace(ele, '*')
print(len(ch))