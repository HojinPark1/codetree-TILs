n=int(input())
cnt = 'A'
for i in range(1, n+1):
    for j in range(1, i):
        print('  ', end='')
    for j in range(n-i+1, 0, -1):
        print(chr(ord(cnt)), end=' ')
        cnt = chr(ord(cnt)+1)
        if ord(cnt)>ord('Z'):
            cnt = "A"
    print()