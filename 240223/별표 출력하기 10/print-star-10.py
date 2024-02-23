n=int(input())
for i in range(0, n*2):
    if i % 2 == 0:
        for j in range(1+(i//2)):
            print("*", end=' ')
    else:
        for j in range(n-(i//2)):
            print("*", end=' ')
    print()