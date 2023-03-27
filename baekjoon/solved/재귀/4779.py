# 칸토어 집합

def Cantor(arr, s, e, arr_len):
    if arr_len == 1: return
    else:
        # 81 -> 1-27, 28-54, 55-81
        # 실제 배열 -> 0-26, 27-53, 54-80
        for i in range(s + int(arr_len/3), s + int(arr_len/3*2)):
            arr[i] = ' '
        Cantor(arr, s, int(arr_len/3)-1, int(arr_len/3))
        Cantor(arr, s + int(arr_len/3)*2, e, int(arr_len/3))

while(1):
    try:
        n = int(input())
        arr = ['-']*pow(3, n)
        Cantor(arr, 0, len(arr)-1, len(arr))
        for i in range(len(arr)):
            print(arr[i], end='')
        print()
    except EOFError:
        break