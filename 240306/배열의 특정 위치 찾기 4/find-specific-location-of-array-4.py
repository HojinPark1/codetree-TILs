r=list(map(int, input().split()))
S=0
A=0

for i in range(10):
    if r[i] == 0:
        break
    elif r[i] % 2 == 0:
        S+=r[i]
        A+=1
    else:
        pass
print(A, S)