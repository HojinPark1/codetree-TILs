n=int(input())
for i in range(n):
    for _ in range(n-i):
        for _ in range(n-i):
            print("*", end='')
        print(end=' ')
    print()