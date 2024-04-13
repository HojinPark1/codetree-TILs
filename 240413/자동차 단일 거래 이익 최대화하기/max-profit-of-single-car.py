n=int(input())
arr=list(map(int, input().split()))
cnt=0
for i in range(n):
    for j in range(i+1, n):
        if arr[j]-arr[i] > 0:
            if cnt < arr[j]-arr[i]:
                cnt = arr[j] - arr[i]
print(cnt)