n= int(input())
for i in range(1, n+1):
    cnt=n-i+1
    for j in range(i):
        print(cnt, end=' ')
        cnt+=1
    print()