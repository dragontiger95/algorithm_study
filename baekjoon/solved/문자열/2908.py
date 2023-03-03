a, b = map(list, input().split())
a[0], a[2] = a[2], a[0]
b[0], b[2] = b[2], b[0]
a = ''.join(a)
b = ''.join(b)
if int(a) > int(b):
    print(a)
else:
    print(b)