n=int(input())
cnt=1
for i in range(1, n+1):
    for j in range(1, n+1):
        if i % 2 != 0:
            if j == n:
                print(cnt, end=' ')
            else:
                print(cnt, end=' ')
                cnt+=1
        elif i % 2 == 0:
            if j == 1:
                cnt+=2
                print(cnt, end=' ')
                cnt+=2
            elif 1 < j < n:
                print(cnt, end=' ')
                cnt+=2
            else:
                print(cnt, end=' ')
                cnt+=1
    print()
