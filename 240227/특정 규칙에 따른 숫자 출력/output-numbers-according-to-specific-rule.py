n=int(input())
cnt=1
for i in range(1, n+1):
    for j in range(i-1):
        print(' ', end= ' ')
    for j in range((n+1-i), 0, -1):
        print(cnt, end=' ')
        cnt+=1
        if cnt>=10:
            cnt=1
    print()