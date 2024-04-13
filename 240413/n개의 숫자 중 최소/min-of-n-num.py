n=int(input())
arr=list(map(int, input().split()))
cnt=0
for i in range(len(arr)):
    if arr[i] == min(arr):
        cnt += 1
print(min(arr), cnt, end=' ')