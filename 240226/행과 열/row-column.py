k=input().split()
a=int(k[0])
b=int(k[1])
for i in range(1, a+1):
    for j in range(1, b+1):
        print(i*j, end=' ')
    print()