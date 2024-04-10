n=int(input())
arr=list(map(int, input().split()))
ans=0
for i in range(n):
    if arr[i] == 2:
        ans += 1
    
    if ans == 3:
        print(i+1)
        break