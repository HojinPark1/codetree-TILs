n=list(map(int, input().split()))
tmp=0
for i in range(10):
    if tmp == 1:
        break
    if n[i] % 3 == 0:
        print(n[i-1])
        tmp+=1