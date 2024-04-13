n=int(input())
arr=list(map(int, input().split()))
arr2=[]
cnt=0

for i in range(len(arr)):
    for j in range(n):
        if i != j and arr[i] == arr[j]:
            pass
        else:
            cnt+=1
            arr2.append(arr[j])

if cnt == 0:
    print(-1)
else:
    print(max(arr2))