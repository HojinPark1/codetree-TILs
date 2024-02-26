n=int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        if i % 2 != 0:
            print(j + (i-1)*n, end=' ')
        else:
            print(n*i-j+1, end=' ')
    print()