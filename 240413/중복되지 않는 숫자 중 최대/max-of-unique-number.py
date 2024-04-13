n=int(input())
arr=list(map(int, input().split()))
arr2=[]

for i in range(len(arr)):
    arr2.append(arr[i])
    for j in range(len(arr)):
        if i != j and arr[i] == arr[j]:
            if arr[i] in arr2:
                arr2.remove(arr[j])
            else:
                pass

if arr2==[]:
    print(-1)
else:
    print(max(arr2))