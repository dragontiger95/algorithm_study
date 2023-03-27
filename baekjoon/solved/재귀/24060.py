# 알고리즘 수업 - 병합 정렬 1

import sys

n, k = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt, ans = 0, 0

def merge(s1, e1, s2, e2):
    global cnt
    global ans
    i = s1
    j = s2
    tmp =  []

    while(i<=e1 and j<=e2):
        if(arr[i] <= arr[j]):
            tmp.append(arr[i])
            i+=1
        else:
            tmp.append(arr[j])
            j+=1

        cnt+=1
        if cnt == k: ans = tmp[len(tmp)-1]
    
    while(i<=e1):
        tmp.append(arr[i])
        i+=1
        cnt+=1
        if cnt == k: ans = tmp[len(tmp)-1]
    while(j<=e2):
        tmp.append(arr[j])
        j+=1
        cnt+=1
        if cnt == k: ans = tmp[len(tmp)-1]

    for idx in range(s1, e2+1):
        arr[idx] = tmp[idx-s1]


def mergeSort(s, e):
    if s>=e: return
    else:
        mid = int((s+e)/2)
        mergeSort(s, mid)
        mergeSort(mid+1, e)
        merge(s, mid, mid+1, e)


mergeSort(0, len(arr)-1)
if cnt < k:
    print(-1)
else:
    print(ans)