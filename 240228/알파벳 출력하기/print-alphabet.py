k=65
n=int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        if k != ord('Z'):
            print(chr(k), end='')
            k+=1
        if k == ord('Z'):
            print(chr(k), end='')
            k=ord('A')
    print()