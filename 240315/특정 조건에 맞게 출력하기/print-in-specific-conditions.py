k=list(map(int, input().split()))
tmp=0
for i in range(100):
    if k[i] ==0:
        break
    else:
        if k[i] % 2 == 1:
            print(k[i]+3, end=' ')
        else:
            print(k[i]//2, end=' ')