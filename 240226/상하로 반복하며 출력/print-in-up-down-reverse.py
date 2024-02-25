n=int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == 1 or j == 3:
            print(i, end='')
        elif j == 2 or j == 4:
            print(n+1-i, end='')
    print()