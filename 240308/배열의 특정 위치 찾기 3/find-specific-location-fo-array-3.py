k=list(map(int, input().split()))
for i in range(100):
    if k[i] == 0:
        print(k[i-1]+k[i-2]+k[i-3])
        break