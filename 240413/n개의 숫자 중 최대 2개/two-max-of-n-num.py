n=int(input())
arr=list(map(int, input().split()))
arr2=[]
for i in arr:
    if i == max(arr):
        pass
    else:
        arr2.append(i)

print(max(arr), max(arr2), end=' ')