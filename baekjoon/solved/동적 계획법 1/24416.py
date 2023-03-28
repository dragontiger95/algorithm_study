# 알고리즘 수업 - 피보나치 수 1
## 재귀로 푼 횟수 = 피보나치 n 번째 수 -> n > 2 인 모든 memo_arr[n]은 memo_arr[1] = 1, memo_arr[2] = 1 값 모음의 총합이 되기 때문
## 재귀 직접 구현해서 풀면 시간초과 ..

n = int(input())

# recursion_cnt = 0
# memo_arr = [0] * (n+1)
# def fibonacci_recursion(n):
#     global recursion_cnt
#     global memo_arr
#     if n==1 or n==2:
#         return 1
#     else:
#         if memo_arr[n] == 0:
#             memo_arr[n] = fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
#         recursion_cnt += 1
#         return memo_arr[n]

# fibonacci_recursion(n)
# print(recursion_cnt, end=' ')


dynamic_cnt = 0
def fibonacci_dynamic(n):
    global dynamic_cnt
    arr = [0] * (n+1)
    arr[1] = 1
    arr[2] = 1
    for i in range(3, n+1):
        arr[i] = arr[i-1] + arr[i-2]
        dynamic_cnt += 1
    return arr[n]

print(fibonacci_dynamic(n), dynamic_cnt)