n=int(input())
k=list(map(int, input().split()))
k2=list()
for i in range(n):
    if k[i] % 2 == 0:
        k2.append(k[i])
    else:
        pass
k2=k2[::-1]
for i in range(len(k2)):
    print(k2[i], end=' ')