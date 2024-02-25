n=int(input())
cnt=9
for i in range(1, n+1):
    for j in range(1, n+1):
        if cnt > 1:
            print(cnt, end='')
            cnt -= 1
        elif cnt == 1:
            print(cnt, end='')
            cnt = 9
    print()