n=int(input())
arr=list(map(int, input().split()))
arr2=[]
cnt=0
for i in arr:
    if i == max(arr):
        if cnt >= 1:
            arr2.append(i)
        cnt += 1
        pass
    else:
        arr2.append(i)

print(max(arr), max(arr2), end=' ')