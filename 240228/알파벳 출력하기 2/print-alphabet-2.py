n=int(input())
k=65
for i in range(1, n+1):
    for j in range(1, i):
        print('  ', end='')
    for j in range(n-i+1, 0, -1):
        print(chr(k), end=' ')
        k+=1
        if k>ord('Z'):
            k=65
    print()