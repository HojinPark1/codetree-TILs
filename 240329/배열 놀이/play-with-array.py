k1=list(map(int, input().split()))
k2=list(map(int, input().split()))
for _ in range(k1[1]):
    k3=list(map(int, input().split()))
    if k3[0] == 1:
        print(k2[k3[1] - 1])
    if k3[0] == 2:
        if k3[1] in k2:
            print(k2.index(k3[1]) + 1)
        else:
            print(0)
    if k3[0] == 3:
        for i in range(k3[1]-1, (k3[2])):
            print(k2[i], end=' ')