n=int(input())
arr=list(map(int, input().split()))
arr2=[]
for i in range(n):
    for j in range(n):
        if arr[i] - arr[j] >0:
            arr2.append(arr[i] - arr[j])

print(min(arr2))